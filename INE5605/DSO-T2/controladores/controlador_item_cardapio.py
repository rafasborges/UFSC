from DAOs.itemCardapio_dao import ItemCardapioDAO
from entidades.itemCardapio import ItemCardapio
from exceptions.item_cardapio_repetido_exception import ItemCardapioRepetidoException
from exceptions.item_nao_existente_exception import ItemNaoExistenteException
from limites.tela_item_cardapio import TelaItemCardapio


class ControladorItemCardapio():
    def __init__(self, controlador_sistema):
        self.__item_cardapio_DAO = ItemCardapioDAO()
        self.__tela_item_cardapio = TelaItemCardapio()
        self.__controlador_sistema = controlador_sistema

    def pega_item_por_cod(self, codigo_item: int):
        for item in self.__item_cardapio_DAO.get_all():
            if(int(item.codigo_item) == int(codigo_item)):
                return item
        return None

    def incluir_item(self):
        dados_item = self.__tela_item_cardapio.pega_dados_item_cardapio()
        if dados_item == None or dados_item["nome"] == "" or dados_item["descricao"] == "" or dados_item["codigo_item"] == 900 or dados_item["preco"] == 900:
            return
        codigo_item = dados_item["codigo_item"]
        item = self.pega_item_por_cod(codigo_item)
        try:
            if item == None:
                item = ItemCardapio(dados_item["nome"], dados_item["descricao"], dados_item["codigo_item"], dados_item["preco"])
                self.__item_cardapio_DAO.add(item)
            else:
                raise ItemCardapioRepetidoException(codigo_item)
        except ItemCardapioRepetidoException as e:
            self.__tela_item_cardapio.mostra_mensagem(e)

    def alterar_item(self):
        self.lista_itens_cardapio()
        cod_item = self.__tela_item_cardapio.seleciona_item()
        if cod_item == None:
            return
        item = self.pega_item_por_cod(cod_item)

        try:
            if(item is not None):
                novos_dados_item = self.__tela_item_cardapio.pega_dados_item_cardapio()
                if novos_dados_item == None or novos_dados_item["codigo_item"] == 0:
                    return
                item.nome = novos_dados_item["nome"]
                item.descricao = novos_dados_item["descricao"]
                item.codigo_item = novos_dados_item["codigo_item"]
                item.preco = novos_dados_item["preco"]
                self.__item_cardapio_DAO.update(item)
                self.lista_itens_cardapio()
            else:
                raise ItemNaoExistenteException(cod_item)
        except ItemNaoExistenteException as a:
            self.__tela_item_cardapio.mostra_mensagem(a)

    def lista_itens_cardapio(self):
        if len(self.__item_cardapio_DAO.get_all()) == 0:
                self.__tela_item_cardapio.mostra_mensagem("ATENÇÃO: Lista de itens vazia")
        dados_itens = []
        for item in self.__item_cardapio_DAO.get_all():
            dados_itens.append({"nome": item.nome, "descricao": item.descricao, "codigo_item": item.codigo_item, "preco": item.preco})
        self.__tela_item_cardapio.mostra_item_cardapio(dados_itens)    

    def lista_itens_cardapio_formatado(self):
        if len(self.__item_cardapio_DAO.get_all()) == 0:
            self.__tela_item_cardapio.mostra_mensagem("ATENÇÃO: Lista de itens vazia")
        dados_itens = []
        for item in self.__item_cardapio_DAO.get_all():
            dados_itens.append({"nome": item.nome, "descricao": item.descricao, "codigo_item": item.codigo_item, "preco": item.preco})
        self.__tela_item_cardapio.mostra_item_cardapio(dados_itens)    

    def excluir_item(self):
        self.lista_itens_cardapio()
        cod_item = self.__tela_item_cardapio.seleciona_item()
        if cod_item == None:
            return
        item = self.pega_item_por_cod(cod_item)

        try:
            if(item is not None):
                self.__item_cardapio_DAO.remove(item.codigo_item)
                self.lista_itens_cardapio()
            else:
                raise ItemNaoExistenteException(cod_item)
        except ItemNaoExistenteException as a:
            self.__tela_item_cardapio.mostra_mensagem(a)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_item, 2: self.alterar_item, 3: self.excluir_item, 4: self.lista_itens_cardapio, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_item_cardapio.tela_opcoes()]()