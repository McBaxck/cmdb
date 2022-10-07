
from dataclasses import dataclass
@dataclass
class Partition():
    _label: str
    _goUnusedMemory: int
    _goUsedMemory: int

    @property
    def label(self) -> str:
        return self._label

    @property
    def goUnusedMemory(self) -> int:
        """
        précondtion: 
        la mémoire non utilisée ne peux pas dépasser la mémoire totale de la partition
        postcondition: 
        La mémoire non utilisée et la mémoire non utilisée doivent être égale à la mémoire totale de la partition
        """
        return self._goUnusedMemory

    @property
    def goUsedMemory(self) -> int:
        """
        précondtion: 
        la mémoire utilisée ne peux pas dépasser la mémoire totale de la partition
        postcondition: 
        La mémoire utilisée et la mémoire non utilisée doivent être égale à la mémoire totale de la partition
        """
        return self._goUsedMemory

    @label.setter
    def label(self, value: str) -> None:
        self._label = value

    @goUnusedMemory.setter
    def goUnusedMemory(self, new_space: int) -> None:
        """
        précondtion: 
        la mémoire non utilisée ne peux pas dépasser la mémoire totale de la partition
        postcondition: 
        La mémoire utilisée et la mémoire non utilisée doivent être égale à la mémoire totale de la partition
        """
        self._goUnusedMemory = new_space

    @goUsedMemory.setter
    def goUsedMemory(self, new_space: int) -> None:
        """
        précondtion: 
        la mémoire utilisée ne peux pas dépasser la mémoire totale de la partition
        postcondition: 
        La mémoire utilisée et la mémoire non utilisée doivent être égale à la mémoire totale de la partition
        """
        self._goUsedMemory = new_space
