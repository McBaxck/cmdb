from dataclasses import dataclass

from classes.server.config.policy import Policy

"""_summary_

    Attributs :
        _id: int
        _ip_source: str
        _ip_destination: str
        _port: int
        _protocol: str
        _option: list
        _iptable_policy: Policy

    Méthodes : 
@invariant: policy enum value(ACCEPT="ACCEPT",DENIED="DENIED",LOG="LOG",DROP="DROP","ALLOWED")

"""
@dataclass
class IpTableRules():
    _id: int
    _ip_source: str
    _ip_destination: str
    _port: int
    _protocol: str
    _option: list
    _iptable_policy: Policy
    
    def __post_init__(self) -> None:
        if type(self._option) == str:
            self._option = [self._option]
            print(self._option)

    @property
    def id(self) -> int:
        return self._id

    @property
    def ip_source(self) ->str:
        return self._ip_source

    @property
    def ip_destination(self) ->str:
        return self._ip_destination

    @property
    def port(self) ->int:
        return self._port

    @property
    def protocol(self) ->str:
        return self._protocol

    @property
    def option(self) ->list:
        return self._option

    @property
    def iptablePolicy(self) -> Policy:
        return self._iptable_policy

    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    @ip_source.setter
    def ip_source(self, value: str) -> None:
        self._ip_source = value

    @ip_destination.setter
    def ip_destination(self, value: str) -> None:
        self._ip_destination = value

    @port.setter
    def port(self, value: int) -> None:
        self._port = value

    @protocol.setter
    def protocol(self, value: str) -> None:
        self._protocol = value

    @option.setter
    def option(self, value: str) -> None:
        print(type(value))
        self._option = value

    @iptablePolicy.setter
    def iptablePolicy(self, value: Policy) -> None:
        self._iptable_policy = value

    def option_append(self, value: str) -> None:
        """permet d'ajouter une valeur dans le tableau option

        Args:
            value (str): valeur à rajouter
        """
        self._option.append(value)
    
    def option_delete(self, value: str) -> None:
        """permet de supprimer la première itération d'une option

        Args:
            value (str): _description à supprimer
        """
        try:
            self._option.remove(value)
        except ValueError:
            pass