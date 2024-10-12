class ItemCardapio:
    def __init__(self, nome: str, descricao: str, codigo_item: int, preco: int):
        self.__nome = nome
        self.__descricao = descricao
        self.__codigo_item = codigo_item
        self.__preco = preco

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao
    
    @property
    def codigo_item(self):
        return self.__codigo_item
    
    @codigo_item.setter
    def codigo_item(self, codigo_item):
        self.__codigo_item = codigo_item
    
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, preco):
        self.__preco = preco