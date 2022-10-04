from dataclasses import dataclass
from ip_table_rules import IpTableRules

@dataclass
class Securite():
    _id: int
    _ipFireWall: str
    _list_ip_table: list

    @property
    def ipFireWall(self) -> str:
        return self._ipFireWall

    @property
    def list_ip_table(self) -> list:
        return self._list_ip_table

    @ipFireWall.setter
    def ipFireWall(self, new_ip: str) -> None:
        self._ipFireWall = new_ip


    def list_ip_table_append(self, id: int, ip_source: str, ip_destination: str, port: int, protocol: str, option: list) -> None:
        """permet de crééer une nouvelle table ip

        Args:
            id (int): id de la table
            ip_source (str): ip_source de la table
            ip_destination (str): ip_destination de la table
            port (int): port de la table
            protocol (str): protocole de la table
            option (list[str]): liste d'option de la table
        """
        self.list_ip_table.append(IpTableRules(id, ip_source, ip_destination, port, protocol, option))


    def list_ip_table_delete(self, id:int) -> None:
        """permet de supprimer la table ip possédant l'id passé en paramètre

        Args:
            id (int): id de l'objet de la liste à supprimer
        """
        for i in range(len(self._list_ip_table)):
            if self.list_ip_table[i].id == id:
                del self.list_ip_table[i]


    def list_ip_table_clear(self)-> None:
        """permet de faire un reste de la la liste des tables ip
        """
        self._list_ip_table = []
