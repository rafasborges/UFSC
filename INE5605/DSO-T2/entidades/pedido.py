from entidades.itemCardapio import ItemCardapio
from entidades.reserva import Reserva


class Pedido:
    def __init__(self, codigo: int, reserva: Reserva, itens: list[ItemCardapio]):
        self.__codigo = codigo
        self.__reserva = reserva
        self.__itens = itens

    
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self,codigo):
        self.__codigo = codigo

    @property
    def reserva(self):
        return self.__reserva
    
    @reserva.setter
    def reserva(self,reserva):
        self.__reserva = reserva

    @property
    def itens(self):
        return self.__itens
    

    