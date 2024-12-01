import json
import pathlib
import sqlite3
from typing import Union, Dict, Optional, List

import appdirs
from ontolutils import Thing
from pydantic import HttpUrl, AnyUrl, EmailStr
from ssnolib import __version__

from pivmetalib.prov import Person
from .abstract_databases import AbstractDatabaseSourceAdapter, DataField


def trim_dict(d):
    trimmed = {k: v for k, v in d.items() if v or v != ''}
    if "id" in trimmed:
        if not trimmed["id"].startswith(("http", "_:")):
            trimmed["id"] = f"_:{trimmed['id']}"
    return trimmed


class JSONLDFileDatabaseSourceAdapter(AbstractDatabaseSourceAdapter):
    """A simple JSON-LD file-based database implementation."""

    def __init__(self, model_cls, file_location: Union[str, pathlib.Path] = None):
        self.name = model_cls.__name__.lower()
        self.model_cls = model_cls  # e.g. prov.Person
        if file_location is None:
            user_data_dir = pathlib.Path(appdirs.user_data_dir('pivmetalib', version=__version__))
            self.db_dir = user_data_dir / self.name
        else:
            self.db_dir = pathlib.Path(file_location)
        self.db_dir.mkdir(parents=True, exist_ok=True)

    def reset(self):
        """Resetting the database, i.e. deleting all files. Cannot be undone!"""
        for filename in self.db_dir.glob('*.jsonld'):
            filename.unlink()

    def fetch_all(self, limit: Optional[int] = None) -> Dict[str, Thing]:
        filenames = sorted(self.db_dir.glob('*.jsonld'))
        persons = [self.model_cls.from_jsonld(source=filename, limit=1) for filename in filenames]
        if limit:
            return {p.id: p for p in persons[0:limit]}
        else:
            return {p.id: p for p in persons}

    def query(self, limit: Optional[int] = None, **kwargs, ) -> List:
        persons = self.fetch_all()
        found_persons = []
        for _, person in persons.items():
            if all(getattr(person, k) == v for k, v in kwargs.items()):
                found_persons.append(person)
        return found_persons

    @property
    def fields(self) -> List[DataField]:
        return [DataField(label=c, datatype="str", required=False) for c in self.model_cls.model_fields.keys()]

    def save(self, data: Thing):
        if not isinstance(data, self.model_cls):
            raise ValueError(f"Data must be an instance of {self.model_cls} but is {type(data)}")

        if data.id:
            existing_entry = self.query(orcidId=data.id)
            if existing_entry:
                print("Not doing anything. Entry already exists.")
                return

        filenames = self.db_dir.glob('*.jsonld')
        n_filenames = len(list(filenames))
        target_filename = self.db_dir / f"{n_filenames + 1:06d}.jsonld"
        with open(target_filename, mode="w", encoding="utf-8") as f:
            json.dump(json.loads(data.model_dump_jsonld()), f, indent=2)

    def delete(self, kwargs):
        for filename in self.db_dir.glob('*.jsonld'):
            person = self.model_cls.from_jsonld(filename)
            if all(getattr(person, k) == v for k, v in kwargs.items()):
                filename.unlink()

    def update(self, data: Thing):
        return self.save(data)


class PersonJSONLDFileDatabase(JSONLDFileDatabaseSourceAdapter):
    def __init__(self, file_location=None):
        super().__init__(Person, file_location=file_location)


class SQLDatabaseSourceAdapter(AbstractDatabaseSourceAdapter):

    def __init__(self, model_cls: Thing, db_uri=None, ignore_fields=None):
        if db_uri is None:
            db_uri = f"{model_cls.__name__}.db"
        self.db_uri = db_uri
        self.name = model_cls.__name__.lower()
        self.model_cls = model_cls
        if ignore_fields is None:
            ignore_fields = []
        _fields = [f for f in self.model_cls.model_fields.keys() if f not in ignore_fields]
        self._fields = []
        for field in _fields:

            if field == "hasParameter":

                self._fields.append({
                    "label": field,
                    "type": "nested",
                    "required": False,
                    "subfields": [{
                        "label": "label",
                        "type": "str",
                        "required": False
                    }, {
                        "label": "value",
                        "type": "str",
                        "required": False
                    }, {
                        "label": "standardName",
                        "type": "str",
                        "required": False
                    }]
                })

            else:

                _dtype = self.model_cls.model_fields[field].annotation
                if _dtype == str:
                    self._fields.append(DataField(label=field, datatype="str", required=False).__dict__)
                elif _dtype == int:
                    self._fields.append(DataField(label=field, datatype="int", required=False).__dict__)
                elif _dtype is HttpUrl or _dtype is AnyUrl:
                    self._fields.append(DataField(label=field, datatype="url", required=False).__dict__)
                elif _dtype is EmailStr:
                    self._fields.append(DataField(label=field, datatype="email", required=False).__dict__)
                else:
                    print(f"Cannot associate datatype with field {field}: {_dtype}")
                    self._fields.append(DataField(label=field, datatype="url", required=False).__dict__)

        self._columns = [self.to_camel_case(s) for s in _fields]
        self._create_table()

    @classmethod
    def to_camel_case(cls, s):
        # Split the string by underscores
        words = s.split('_')

        # Capitalize the first letter of each word (except the first one)
        camel_case = words[0] + ''.join(word.capitalize() for word in words[1:])

        return camel_case

    @property
    def fields(self) -> List[DataField]:
        print(self._fields)
        return self._fields

    def _create_table(self):
        columns = ", ".join(f"{self.to_camel_case(k)} TEXT" for k in self.columns)
        # create tables if not exist:
        with sqlite3.connect(self.db_uri) as conn:
            cursor = conn.cursor()
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.name} ({columns})")

    def reset(self):
        with sqlite3.connect(self.db_uri) as conn:
            cursor = conn.cursor()
            cursor.execute(f"DROP TABLE IF EXISTS {self.name}")
            conn.commit()
        self._create_table()

    @property
    def columns(self):
        return self._columns

    def fetch_all(self, limit: Optional[int] = None) -> Dict[str, Thing]:
        fields = ", ".join(self.columns)
        with sqlite3.connect(self.db_uri) as conn:
            cursor = conn.cursor()
            if limit:
                cursor.execute(f"SELECT {fields} FROM {self.name} LIMIT {limit}")
            else:
                cursor.execute(f"SELECT {fields} FROM {self.name}")
            rows = cursor.fetchall()

        if not rows:
            return {}
        list_of_data_dicts = [{k: v for k, v in zip(self.columns, row)} for row in rows]
        things = [self.model_cls.model_validate({k: v for k, v in data_dict.items() if v}) for data_dict in
                  list_of_data_dicts]
        return {thing.id: thing for thing in things}

    def query(self, limit: Optional[int] = None, **kwargs) -> List:

        if not kwargs:
            return self.fetch_all(limit=limit)

        base_query = f"SELECT * FROM {self.name}"

        where_clause = " AND ".join([f"{k} = '{v}'" for k, v in kwargs.items()])

        if limit:
            query = f"{base_query} WHERE {where_clause} LIMIT {limit};"
        else:
            query = f"{base_query} WHERE {where_clause};"

        # Execute the query and fetch the result
        with sqlite3.connect(self.db_uri) as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            if limit:
                rows = cursor.fetchmany(limit)
            else:
                rows = cursor.fetchall()
        res = []
        for row in rows:
            data_dict = {k: v for k, v in zip(self.columns, row)}
            res.append(self.model_cls.model_validate({k: v for k, v in data_dict.items() if v}))
        return res

    def delete(self, **kwargs):

        if not kwargs:
            raise ValueError("You must provide a query to delete data.")

        base_query = f"DELETE FROM {self.name}"

        where_clause = " AND ".join([f"{k} = '{v}'" for k, v in kwargs.items()])

        query = f"{base_query} WHERE {where_clause};"

        # Execute the query and fetch the result
        with sqlite3.connect(self.db_uri) as conn:
            cursor = conn.cursor()
            cursor.execute(query)

    def save(self, data: Thing):
        # Save or update a person entry
        data_dict = data.model_dump(exclude_none=True)
        fields = ", ".join(self.to_camel_case(s) for s in data_dict.keys())
        data_list = list(data_dict.values())
        qs = ", ".join("?" for _ in data_list)
        with sqlite3.connect(self.db_uri) as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
                INSERT OR REPLACE INTO {self.name} ({fields}) 
                VALUES ({qs})
            """, data_list)
            conn.commit()

    def update(self, data: Thing):
        pass


class LaserMongoDatabaseSourceAdapter(AbstractDatabaseSourceAdapter):
    def __init__(self, collection: "Collection"):
        self.collection = collection

    def fetch_all(self, limit: Optional[int] = None) -> Dict[str, Thing]:
        pass

    def fields(self) -> List[DataField]:
        pass

    def reset(self):
        pass

    def delete(self, **kwargs):
        pass

    def query(self, limit: Optional[int] = None, **kwargs) -> List:
        pass

    def save(self, data: Thing):
        pass

    def update(self, data: Thing):
        pass

# class LaserSQLDatabase(AbstractDatabase):
#     def __init__(self, db_uri=None):
#         if db_uri is None:
#             db_uri = "laser.db"
#         assert db_uri.endswith(".db"), "Database URI must end with .db"
#         self.db_uri = db_uri
#         self.name = "laser"
#         # self._columns = ["waveLength", "power", "pulseDuration", "pulseEnergy", "beamDiameter",]
#         self._columns = ["id", "label", "wikidataLink", "waveLength", "pulseEnergy"]
#         self._create_table()
#
#     @property
#     def columns(self):
#         return self._columns
#
#     def _create_table(self):
#         columns = ", ".join(f"{k} TEXT" for k in self.columns)
#         # create tables if not exist:
#         with sqlite3.connect(self.db_uri) as conn:
#             cursor = conn.cursor()
#             cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.name} ({columns})")
#
#     def fetch_all(self, limit: Optional[int] = None) -> Dict[str, Thing]:
#         fields = ", ".join(self.columns)
#         with sqlite3.connect(self.db_uri) as conn:
#             cursor = conn.cursor()
#             if limit:
#                 cursor.execute(f"SELECT {fields} FROM {self.name} LIMIT {limit}")
#             else:
#                 cursor.execute(f"SELECT {fields} FROM {self.name}")
#             rows = cursor.fetchall()
#
#         if not rows:
#             return {}
#         list_of_data_dicts = [{k: v for k, v in zip(self.columns, row)} for row in rows]
#         for data_dict in list_of_data_dicts:
#             print(data_dict)
#         things = [Laser.model_validate({k: v for k, v in data_dict.items() if v}) for data_dict in
#                   list_of_data_dicts]
#         return {thing.id: thing for thing in things}
#
#     def reset(self):
#         with sqlite3.connect(self.db_uri) as conn:
#             cursor = conn.cursor()
#             cursor.execute(f"DROP TABLE IF EXISTS {self.name}")
#             conn.commit()
#         self._create_table()
#
#     def delete(self, **kwargs):
#         pass
#
#     def query(self, limit: Optional[int] = None, **kwargs) -> List:
#         pass
#
#     def save(self, data: Laser):
#         # Save or update a person entry
#
#         parameters = {}
#         if data.hasParameter:
#             if not isinstance(data.hasParameter, list):
#                 _parameters = [data.hasParameter]
#             for param in _parameters:
#                 name = param
#                 if isinstance(param, str):
#
#             if "waveLength" in data.:
#         data_dict = {
#             "label": data.label,
#         }
#
#         data_dict = data.model_dump(exclude_none=True)
#         fields = ", ".join(s for s in data_dict.keys())
#         data_list = list(data_dict.values())
#         qs = ", ".join("?" for _ in data_list)
#         with sqlite3.connect(self.db_uri) as conn:
#             cursor = conn.cursor()
#             cursor.execute(f"""
#                 INSERT OR REPLACE INTO {self.name} ({fields})
#                 VALUES ({qs})
#             """, data_list)
#             conn.commit()
#
#     def update(self, data: Laser):
#         pass
