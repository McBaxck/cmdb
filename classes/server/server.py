from dataclasses import dataclass, asdict
from typing import List
from classes.server.config.interface_reseau import InterfaceReseau
from classes.server.stockage.raid import RAID
from classes.server.config.securite import Securite
from dd import HardDisk
from abc import ABC

    """_summary_

    Attributs :
        _label: str
        _moRam: int
        _cpu: str
        _gpu: str
        _hostname: str
        _disks: List[HardDisk]
        _interface_reseau: List[InterfaceReseau]
        _securite: List[Securite]
        _raid: List[RAID]
    
    Methodes : 
        label(self) -> str
        moRam(self) -> int
        cpu(self) -> str
        gpu(self) -> str
        hostname(self) -> str
        disks(self) -> List[HardDisk]
        interfaceReseau(self) -> List[InterfaceReseau]
        securite(self) -> List[Securite]

        @invariant: raid enum value ("RAID_0","RAID_1","RAID_2","RAID_5","RAID_6")
        RAID(self) -> List[RAID]

    """
@dataclass
class Server(ABC):
    _label: str
    _moRam: int
    _cpu: str
    _gpu: str
    _hostname: str
    _disks: List[HardDisk]
    _interface_reseau: List[InterfaceReseau]
    _securite: List[Securite]
    _raid: List[RAID]

    @property
    def label(self) -> str:
        return self._label

    @property
    def moRam(self) -> int:
        return self._moRam

    @property
    def cpu(self) -> str:
        # précondition : none
        # post condition : 
        # nombre de coeurs compris 1 et 42
        # nombre de processeur logique entre 1 et 84
        return self._cpu

    @property
    def gpu(self) -> str:
        # précondition : none
        # post condition :
        # mémoire vive entre 16 Mo et 48 Go
        # fréquence entre 0.6 GHz et 5.9 GHz
        return self._gpu

    @property
    def hostname(self) -> str:
        return self._hostname

    @property
    def disks(self) -> List[HardDisk]:
        # précondition : 
        # type doit être soit HDD, soit SSD, soit SSHD
        # taille mémoire comprise entre 512 Mo et 32 To
        # post condition : none
        return self._disks

    @property
    def interfaceReseau(self) -> List[InterfaceReseau]:
        return self._interface_reseau

    @property
    def securite(self) -> List[Securite]:
        return self._securite

    @property
    def RAID(self) -> List[RAID]:
        return self._raid

    @label.setter
    def label(self, value: str) -> None:
        self._label = value

    @moRam.setter
    def moRam(self, value: int) -> None:
        self._moRam = value

    @cpu.setter
    def cpu(self, value: str) -> None:
        # précondition : 
        # nombre de coeurs compris 1 et 42
        # nombre de processeur logique entre 1 et 84
        # post condition : none
        self._cpu = value

    @gpu.setter
    def gpu(self, value: str) -> None:
        # précondition : 
        # mémoire vive entre 16 Mo et 48 Go
        # fréquence entre 0.6 GHz et 5.9 GHz
        # post condition : none 
        self._gpu = value

    @hostname.setter
    def hostname(self, value: str) -> None:
        self._hostname = value

    @disks.setter
    def disks(self, value: List[HardDisk]) -> None:
        # précondition : none
        # post condition :
        # type doit être soit HDD, soit SSD, soit SSHD
        # taille mémoire comprise entre 512 Mo et 32 To
        self._disks = value

    @interfaceReseau.setter
    def interfaceReseau(self, value: List[InterfaceReseau]) -> None:
        self._interface_reseau = value

    @securite.setter
    def securite(self, value: List[Securite]) -> None:
        self._securite = value

    @RAID.setter
    def RAID(self, value: List[RAID]) -> None:
        self._raid = value

    def __str__(self) -> str:
        return self._cpu

    def __len__(self) -> int:
        return len(self._disks)


if __name__ == '__main__':
    test: Server = Server('_label', 392983, '_cpu', '_gpu', '_hostname', [])
    print(asdict(test))
    print(len(test))
