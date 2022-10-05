from cgi import test
from dataclasses import dataclass
from ..GenericFactory import GenericFactory

@dataclass
class Interface_Reseau_Factory(GenericFactory):
    _interface : InterfaceReseau = InterfaceReseau(1,'192.168.0.1',80,'10.0.0.2',[])

    @test
    def test_ipSource(self):
        assert self._interface.ipSource == '192.168.0.1'


it = Interface_Reseau_Factory()
it.test_ipSource()
