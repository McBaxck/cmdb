from dataclasses import dataclass
from partition import Partition
from typing import List

<<<<<<< HEAD
"""_summary_
    La classe HardDisk est une composition de la classe Server
"""
=======

>>>>>>> be6dce35588ad05356728b2c0e7e96a9d009fc30
@dataclass
class HardDisk():
    _label: str
    _goUnusedMemory: int
    _goUsedMemory: int
    _partitions: List[Partition]

    @property
    def label(self) -> str:
        return self._label

    @property
    def goUnusedMemory(self) -> int:
        """
        précondtion: 
        la mémoire non utilisée ne peux pas dépasser la mémoire totale du disque dur
        postcondition: 
        None
        """
        return self._goUnusedMemory

    @property
    def goUsedMemory(self) -> int:
        """
        précondtion: 
        la mémoire utilisée ne peux pas dépasser la mémoire totale du disque dur
        postcondition: 
        None
        """
        return self._goUsedMemory

    @label.setter
    def label(self, value: str) -> None:
        """
        précondtion: 
        None
        postcondition: 
        Ne doit pas être vide
        """
        self._label = value

    @goUnusedMemory.setter
    def goUnusedMemory(self, new_space: int) -> None:
        """
        précondtion: 
        la mémoire non utilisée ne peux pas dépasser la mémoire totale du disque dur
        postcondition: 
        La mémoire utilisée et la mémoire non utilisée doivent être égale à la mémoire totale du disque dur
        """
        self._goUnusedMemory = new_space

    @goUsedMemory.setter
    def goUsedMemory(self, new_space: int) -> None:
        """
        précondtion: 
        la mémoire utilisée ne peux pas dépasser la mémoire totale du disque dur
        postcondition: 
        La mémoire utilisée et la mémoire non utilisée doivent être égale à la mémoire totale du disque dur
        """
        self._goUsedMemory = new_space
