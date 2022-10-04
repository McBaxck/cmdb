from server import Server


class VirtualMachine(Server):
    pass


if __name__ == '__main__':
    test: VirtualMachine = VirtualMachine('', 33737, '', '', '', [])
