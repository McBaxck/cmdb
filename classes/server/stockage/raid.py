import enum

"""_summary_
Classe permettant de définir la clause d'invariance pour l'attribut RAID de l'objet Server
Notons que les contraintes d'invariance sont les valeurs possibles de l'enum 
Cf. server.py
"""
class RAID(enum.Enum):
    RAID_0="RAID_0",
    RAID_1="RAID_1",
    RAID_2="RAID_2",
    RAID_5="RAID_5",
    RAID_6="RAID_6"
