from dataclasses import dataclass, asdict
from typing import Union
from ipaddress import IPv4Address, IPv6Address, ip_address


@dataclass
class Route():
    _ipDestination: str
    _networkMask: int
    _ipBridge: str
    _ipInterface: str
    _ttl: int

    def __post_init__(self) -> None:
        self._ipDestination = ip_address(self._ipDestination)
        self._ipBridge = ip_address(self._ipBridge)
        self._ipInterface = ip_address(self._ipInterface)

    @property
    def ipDestination(self) -> Union[IPv4Address, IPv6Address]:
        return self._ipDestination

    @property
    def ipBridge(self) -> Union[IPv4Address, IPv6Address]:
        return self._ipBridge

    @property
    def ipInterface(self) -> Union[IPv4Address, IPv6Address]:
        return self._ipInterface

    @property
    def networkMask(self) -> int:
        return self._networkMask

    @property
    def ttl(self) -> int:
        return self._ttl

    @ipDestination.setter
    def ipDestination(self, ip: str) -> None:
        self._ipDestination = ip_address(ip)

    @ipBridge.setter
    def ipDestination(self, ip: str) -> None:
        self._ipBridge = ip_address(ip)

    @ipInterface.setter
    def ipInterface(self, ip: str) -> None:
        self._ipInterface = ip_address(ip)

    @networkMask.setter
    def networkMask(self, new_mask: int) -> None:
        self._networkMask = new_mask

    @ttl.setter
    def ttl(self, value: int) -> None:
        self._ttl = value


if __name__ == '__main__':
    test: Route = Route('192.168.1.16', '_networkMask',
                        '_ipBridge', '_ipInterface', 64)
    print(asdict(test))
