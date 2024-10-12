from DAOs.dao import DAO
from entidades.pessoa import Pessoa

class PessoaDAO(DAO):
    def __init__(self):
        super().__init__('pessoa.pkl')

    def add(self, pessoa: Pessoa):
        if((pessoa is not None) and isinstance(pessoa, Pessoa) and isinstance(pessoa.id, int)):
            super().add(pessoa.id, pessoa)

    def update(self, pessoa: Pessoa):
        if((pessoa is not None) and isinstance(pessoa, Pessoa) and isinstance(pessoa.id, int)):
            super().update(pessoa.id, pessoa)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)