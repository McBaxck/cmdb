
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
        return self._goUnusedMemory

    @property
    def goUsedMemory(self) -> int:
        return self._goUsedMemory

    @label.setter
    def label(self, value: str) -> None:
        self._label = value

    @goUnusedMemory.setter
    def goUnusedMemory(self, new_space: int) -> None:
        self._goUnusedMemory = new_space

    @goUsedMemory.setter
    def goUsedMemory(self, new_space: int) -> None:
        self._goUsedMemory = new_space
