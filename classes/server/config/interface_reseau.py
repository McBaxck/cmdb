from dataclasses import dataclass
from typing import List

from classes.server.config.interface_reseau_route import InterfaceReseauRoute


@dataclass
class InterfaceReseau():
    _idInterfaceReseau: int
    _ipSource: str
    _port: int
    _passerelle: str
    _interface_reseau_route: List[InterfaceReseauRoute]

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
    def interfaceReseauRoute(self) -> List[InterfaceReseauRoute]:
        return self._interface_reseau_route

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

    @interfaceReseauRoute.setter
    def interfaceReseauRoute(self, value: List[InterfaceReseauRoute]) -> None:
        self._interface_reseau_route = value