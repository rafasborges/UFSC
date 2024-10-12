from entidades.pessoa import Pessoa


class Funcionario(Pessoa):
    def __init__(self, nome: str, cpf: str, salario: float):
        super().__init__(nome, cpf)
        self.__salario = salario
        self.__comissao = 0

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario):
        self.__salario = salario

    @property
    def comissao(self):
        return self.__comissao

    @comissao.setter
    def comissao(self, comissao):
        self.__comissao = comissao