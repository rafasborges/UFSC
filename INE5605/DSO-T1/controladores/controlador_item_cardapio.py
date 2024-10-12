from entidades.itemCardapio import ItemCardapio
from exceptions.item_cardapio_repetido_exception import ItemCardapioRepetidoException
from exceptions.item_nao_existente_exception import ItemNaoExistenteException
from limites.tela_item_cardapio import TelaItemCardapio


class ControladorItemCardapio():
    def __init__(self, controlador_sistema):
        self.__itens_cardapio = []
        self.__tela_item_cardapio = TelaItemCardapio()
        self.__controlador_sistema = controlador_sistema

    def pega_item_por_cod(self, codigo_item: int):
        for item in self.__itens_cardapio:
            if(int(item.codigo_item) == int(codigo_item)):
                return item
        return None

    def incluir_item(self):
        dados_item = self.__tela_item_cardapio.pega_dados_item_cardapio()
        codigo_item = dados_item["codigo_item"]
        item = self.pega_item_por_cod(codigo_item)
        try:
            if item == None:
                item = ItemCardapio(dados_item["nome"], dados_item["descricao"], dados_item["codigo_item"], dados_item["preco"])
                self.__itens_cardapio.append(item)
            else:
                raise ItemCardapioRepetidoException(codigo_item)
        except ItemCardapioRepetidoException as e:
            self.__tela_item_cardapio.mostra_mensagem(e)

    def alterar_item(self):
        self.lista_itens_cardapio()
        cod_item = self.__tela_item_cardapio.seleciona_item()
        item = self.pega_item_por_cod(cod_item)

        try:
            if(item is not None):
                novos_dados_item = self.__tela_item_cardapio.pega_dados_item_cardapio()
                item.nome = novos_dados_item["nome"]
                item.descricao = novos_dados_item["descricao"]
                item.codigo_item = novos_dados_item["codigo_item"]
                item.preco = novos_dados_item["preco"]
                self.lista_itens_cardapio()
            else:
                raise ItemNaoExistenteException(cod_item)
        except ItemNaoExistenteException as a:
            self.__tela_item_cardapio.mostra_mensagem(a)

    def lista_itens_cardapio(self):
        self.__tela_item_cardapio.mostra_mensagem("------ITENS------")
        if len(self.__itens_cardapio) == 0:
                self.__tela_item_cardapio.mostra_mensagem("ATENÇÃO: Lista de itens vazia")
        for item in self.__itens_cardapio:
            self.__tela_item_cardapio.mostra_item_cardapio({"nome": item.nome, "descricao": item.descricao, "codigo_item": item.codigo_item, "preco": item.preco})

    def lista_itens_cardapio_formatado(self):
        if len(self.__itens_cardapio) == 0:
                self.__tela_item_cardapio.mostra_mensagem("ATENÇÃO: Lista de itens vazia")
        for item in self.__itens_cardapio:
            self.__tela_item_cardapio.mostra_item_cardapio_formatado({"nome": item.nome, "descricao": item.descricao, "codigo_item": item.codigo_item, "preco": item.preco})

    def excluir_item(self):
        self.lista_itens_cardapio()
        cod_item = self.__tela_item_cardapio.seleciona_item()
        item = self.pega_item_por_cod(cod_item)

        try:
            if(item is not None):
                self.__itens_cardapio.remove(item)
                self.lista_itens_cardapio()
            else:
                raise ItemNaoExistenteException(cod_item)
        except ItemNaoExistenteException as a:
            self.__tela_item_cardapio.mostra_mensagem(a)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_item, 2: self.alterar_item, 3: self.excluir_item, 4: self.lista_itens_cardapio, 5: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_item_cardapio.tela_opcoes()]()