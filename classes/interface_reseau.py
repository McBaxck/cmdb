from dataclasses import dataclass


@dataclass
class InterfaceReseau():
    _ipSource: str
    _port: int
    _passerelle: str

    @property
    def ipSource(self) -> str:
        return self._ipSource

    @property
    def port(self) -> int:
        return self._port

    @property
    def passerelle(self) -> int:
        return self._passerelle

    @ipSource.setter
    def ipSource(self, value: str) -> None:
        self._ipSource = value

    @port.setter
    def port(self, value: int) -> None:
        self._port = value

    @passerelle.setter
    def passerelle(self, value: str) -> None:
        self._passerelle = value
