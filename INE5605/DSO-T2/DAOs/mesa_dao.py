from DAOs.dao import DAO
from entidades.mesa import Mesa

class MesaDAO(DAO):
    def __init__(self):
        super().__init__('mesas.pkl')

    def add(self, mesa: Mesa):
        if((mesa is not None) and isinstance(mesa, Mesa) and isinstance(mesa.numero, int)):
            super().add(mesa.numero, mesa)

    def update(self, mesa: Mesa):
        if((mesa is not None) and isinstance(mesa, Mesa) and isinstance(mesa.numero, int)):
            super().update(mesa.numero, mesa)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)