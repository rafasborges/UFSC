from entidades.cliente import Cliente
from entidades.funcionario import Funcionario
from entidades.mesa import Mesa


class Reserva:
    def __init__(self, id: int, cliente: Cliente, funcionario: Funcionario, mesa: Mesa):
        self.__id = id
        self.__cliente = cliente
        self.__funcionario = funcionario
        self.__mesa = mesa 
    
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def funcionario(self):
        return self.__funcionario

    @funcionario.setter
    def funcionario(self, funcionario):
        self.__funcionario = funcionario

    @property
    def mesa(self):
        return self.__mesa

    @mesa.setter
    def mesa(self, mesa):
        self.__mesa = mesa


