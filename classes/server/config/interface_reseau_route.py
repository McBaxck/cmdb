from dataclasses import dataclass

@dataclass
class InterfaceReseauRoute():
    _id_interface_reseau_route: int
    _ip_destination: str
    _masque_reseau: str
    _ip_interface: str
    _ttl: int

    @property
    def id(self) -> int:
        return self._id_interface_reseau_route

    @property
    def ipDestination(self) -> str:
        return self._ip_destination

    @property
    def masqueReseau(self) -> str:
        return self._masque_reseau

    @property
    def ipInterface(self) -> str:
        return self._ip_interface

    @property
    def ttl(self) -> int:
        return self._ttl

    @id.setter
    def id(self, value: int) -> None:
        self._id_interface_reseau_route = value

    @ipDestination.setter
    def ipDestination(self, value: str) -> None:
        self._ip_destination = value

    @masqueReseau.setter
    def masqueReseau(self, value: str) -> None:
        self._masque_reseau = value

    @ipInterface.setter
    def ipInterface(self, value: str) -> None:
        self._ip_interface = value

    @ttl.setter
    def ttl(self, value: int) -> None:
        self._ttl = value