from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Any

"""_summary_
    Interface CRUD
    interface de liaison par défaut à la base de données
"""
@dataclass
class IDatabase(ABC):

    @abstractmethod
    def create(self, T: Any) -> Any:
        pass

    @abstractmethod
    def update(self, T: Any) -> Any:
        pass

    @abstractmethod
    def delete(self, T: Any) -> Any:
        pass

    @abstractmethod
    def selectAll(self) -> Any:
        pass

    @abstractmethod
    def selectById(self, id: int) -> Any:
        pass

    @abstractmethod
    def selectLastId(self) -> Any:
        pass
