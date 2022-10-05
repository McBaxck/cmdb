import enum

"""_summary_
Classe permettant de définir la clause d'invariance pour l'attribut policy de l'objet IpTableRules
Notons que les contraintes d'invariance sont les valeurs possibles de l'enum 
Cf. ip_table_reseau.py
"""
class Policy(enum.Enum):
    ACCEPT="ACCEPT",
    DENIED="DENIED",
    LOG="LOG",
    DROP="DROP",
    ALLOWED="ALLOWED"
