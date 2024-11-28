from abc import ABC, abstractmethod
from typing import Dict, Optional, List

from ontolutils import Thing


class AbstractDatabase(ABC):
    @abstractmethod
    def fetch_all(self, limit:Optional[int]=None) -> Dict[str, Thing]:
        """Fetch all entries."""
        pass

    @abstractmethod
    def query(self, limit:Optional[int]=None, **kwargs) -> List:
        """query entries by keyword arguments (table column and value)."""
        pass

    @abstractmethod
    def save(self, data: Thing):
        """Save or update an object."""
        pass

    @abstractmethod
    def delete(self,**kwargs):
        """Delete an object."""
        pass

    @abstractmethod
    def update(self, data: Thing):
        """Save or update an object."""
        pass
