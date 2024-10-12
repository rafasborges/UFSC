from entidades.pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome: str, cpf: str, idade: int, num_convidados: int):
        super().__init__(nome, cpf)
        self.__idade = idade
        self.__num_convidados = num_convidados

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def num_convidados(self):
        return self.__num_convidados

    @num_convidados.setter
    def num_convidados(self, num_convidados):
        self.__num_convidados = num_convidados