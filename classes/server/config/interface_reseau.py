from dataclasses import dataclass


@dataclass
class InterfaceReseau():
    _idInterfaceReseau: int
    _ipSource: str
    _port: int
    _passerelle: str
    _idServer: int

    @property
    def idInterfaceReseau(self) -> int:
        return self._idInterfaceReseau

    @property
    def ipSource(self) -> str:
        return self._ipSource

    @property
    def port(self) -> int:
        return self._port

    @property
    def passerelle(self) -> int:
        return self._passerelle

    @property
    def idServer(self) -> int:
        return self._idServer

    @idInterfaceReseau.setter
    def idInterfaceReseau(self, value: int) -> None:
        self._idInterfaceReseau = value

    @ipSource.setter
    def ipSource(self, value: str) -> None:
        self._ipSource = value

    @port.setter
    def port(self, value: int) -> None:
        self._port = value

    @passerelle.setter
    def passerelle(self, value: str) -> None:
        self._passerelle = value

    @idServer.setter
    def ipServer(self, value: int) -> None:
        self._idServer = value
