from dataclasses import dataclass
from typing import List


@dataclass
class Server():
    _label: str
    _moRam: int
    _cpu: str
    _gpu: str
    _hostname: str

    @property
    def label(self) -> str:
        return self._label

    @property
    def moRam(self) -> int:
        return self._moRam

    @property
    def cpu(self) -> str:
        return self._cpu

    @property
    def gpu(self) -> str:
        return self._gpu

    @property
    def hostname(self) -> str:
        return self._hostname

    @label.setter
    def label(self, value: str) -> None:
        self._label = value

    @moRam.setter
    def moRam(self, value: int) -> None:
        self._moRam = value

    @cpu.setter
    def cpu(self, value: str) -> None:
        self._cpu = value

    @gpu.setter
    def gpu(self, value: str) -> None:
        self._gpu = value

    @hostname.setter
    def hostname(self, value: str) -> None:
        self._hostname = value
