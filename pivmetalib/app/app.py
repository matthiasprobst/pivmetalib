import json
import pathlib

import appdirs
from flask import Flask, render_template, request, redirect, url_for

from pivmetalib import __version__
from pivmetalib.app.abstract_databases import AbstractDatabase
from pivmetalib.app.example_databases import SQLDatabase
from pivmetalib.pivmeta import Laser
from pivmetalib.prov import Person

USER_DATA_DIR = pathlib.Path(appdirs.user_data_dir('pivmetalib', version=__version__))
USER_DATA_DIR.mkdir(parents=True, exist_ok=True)


def trim_dict(d):
    trimmed = {k: v for k, v in d.items() if v or v != ''}
    if "id" in trimmed:
        if not trimmed["id"].startswith(("http", "_:")):
            trimmed["id"] = f"_:{trimmed['id']}"
    return trimmed


def create_app(
        person_database: AbstractDatabase,
        # laser_database: AbstractDatabase
):
    webapp = Flask(__name__)
    webapp.config["databases"] = {}
    webapp.config["databases"]["person"] = person_database
    # webapp.config["databases"]["laser"] = laser_database
    webapp.config["current_person"] = {"id": "", "orcidId": "", "firstName": "", "lastName": ""}

    @webapp.route('/')
    def index():
        return render_template('index.html')

    # @webapp.route('/pivSetup', methods=['GET', 'POST'])
    # def pivsetup_page():
    #     # if topic not in data_storage:
    #     #     return "Invalid topic", 404
    #
    #     # if request.method == 'POST':
    #     #     # Retrieve form data
    #     #     name = request.form.get('name')
    #     #     id = request.form.get('id')
    #     #
    #     #     # Save the data
    #     #     data_storage[topic] = {"name": name, "id": id}
    #     #
    #     #     # Check which button was pressed
    #     #     if 'save_exit' in request.form:
    #     #         return redirect(url_for('landing_page'))
    #     #     elif 'preview' in request.form:
    #     #         return render_template('preview.html', topic=topic, data=data_storage[topic])
    #
    #     # GET: Render the topic page
    #     return render_template('pivSetup/index.html', data=data_storage["pivSetup"])

    @webapp.route('/laser', methods=['GET', 'POST'])
    def laser_page():
        database = webapp.config["databases"]["laser"]
        data = database.fetch_all()
        current_selection = webapp.config["current_selection"]["laser"] = {"id": "", "name": "", "wavelength": ""}
        return render_template('laser/index.html', current_selection=current_selection, lasers=data)

    @webapp.route('/person', methods=['GET', 'POST'])
    def person_page():
        database = webapp.config["databases"]["person"]
        current_person = webapp.config["current_person"]

        persons = database.fetch_all()
        persons_dict = [{"id": p.id, "orcidId": p.orcidId, "firstName": p.firstName, "lastName": p.lastName} for p in
                        persons.values()]

        if request.method == 'POST':
            # Save form data
            current_person['id'] = request.form.get('id', '')
            current_person['orcidId'] = request.form.get('orcidId', '')
            current_person['firstName'] = request.form.get('firstName', '')
            current_person['lastName'] = request.form.get('lastName', '')

            if any({k: v for k, v in current_person.items() if v != ''}):
                print(f'Saving to {database}')
                database.save(Person(**trim_dict(current_person)))
                for p in database.fetch_all():
                    print(f" > {p}")

            # Check which button was pressed
            if 'save' in request.form:
                return redirect(url_for('person_page'))
            elif "delete" in request.form:
                database.delete(id=current_person["id"])
                webapp.config["current_person"] = {"id": "", "orcidId": "", "firstName": "", "lastName": ""}
                return redirect(url_for('person_page'))
                # return redirect(url_for('index'))
            elif 'preview' in request.form:
                return redirect(url_for('person_preview'))

            # Save to data storage (overwrite if ORCID matches, otherwise add new)
            for person in persons_dict:
                if person['orcidId'] == current_person['orcidId']:
                    person.update(current_person)
                    break
            else:
                persons_dict.append(current_person.copy())

        return render_template('person/index.html', data=current_person, persons=persons_dict)

    @webapp.route('/person/preview')
    def person_preview():
        current_person = webapp.config["current_person"]
        clean_current_person = {k: v for k, v in current_person.items() if v}
        person = Person(
            **clean_current_person
        )
        return render_template('person/preview.html', json_ld=json.loads(person.model_dump_jsonld()))

    return webapp


if __name__ == '__main__':
    person_json_file_location = USER_DATA_DIR / 'tmp/databases/person'
    person_json_file_location.mkdir(parents=True, exist_ok=True)
    # person_db = PersonJSONLDFileDatabase(file_location=person_json_file_location)
    person_db = SQLDatabase(Person)
    # laser_db = LaserSQLDatabase(Laser)
    # person_db.reset()
    webapp = create_app(
        person_database=person_db,
        # laser_database=laser_db
    )
    webapp.run(debug=True)
