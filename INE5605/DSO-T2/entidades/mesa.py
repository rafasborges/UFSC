class Mesa:
    def __init__(self, numero: int, capacidade: int):
        self.__numero = numero
        self.__capacidade = capacidade
        self.__status = False

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def capacidade(self):
        return self.__capacidade

    @capacidade.setter
    def capacidade(self, capacidade):
        self.__capacidade = capacidade
    
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status
        