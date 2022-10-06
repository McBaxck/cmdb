from server import Server

"""_summary_
Classe permettant de définir une contrainte de type pour les classes qui seront de type VirtualMachine
Cf. la classe mère est la classe Server

La classe VirtualMachine hérite de la classe Server
"""
class VirtualMachine(Server):
    pass


if __name__ == '__main__':
    test: VirtualMachine = VirtualMachine('', 33737, '', '', '', [])
