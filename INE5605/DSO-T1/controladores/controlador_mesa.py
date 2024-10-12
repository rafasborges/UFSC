from entidades.mesa import Mesa
from exceptions.mesa_nao_existente_exception import MesaNaoExistenteException
from limites.tela_mesa import TelaMesa
from exceptions.mesa_repetida_exception import MesaRepetidaException


class ControladorMesa():
    def __init__(self, controlador_sistema):
        self.__mesas = []
        self.__tela_mesa = TelaMesa()
        self.__controlador_sistema = controlador_sistema
    
    def pega_mesa_por_numero(self, numero: int):
        for mesa in self.__mesas:
            if(mesa.numero == int(numero)):
                return mesa
        return None

    def incluir_mesa(self):
        dados_mesa = self.__tela_mesa.pega_dados_mesa()
        numero = dados_mesa["numero"]
        capacidade = dados_mesa["capacidade"]
        mesa = self.pega_mesa_por_numero(numero)
        try:
            if mesa == None:
                mesa = Mesa(dados_mesa["numero"], dados_mesa["capacidade"])
                self.__mesas.append(mesa)
            else:
                raise MesaRepetidaException(numero)
        except MesaRepetidaException as e:
            self.__tela_mesa.mostra_mensagem(e)

    def alterar_mesa(self):
        self.lista_mesas()
        numero_mesa = self.__tela_mesa.seleciona_mesa()
        mesa = self.pega_mesa_por_numero(numero_mesa)

        try:
            if(mesa is not None):
                novos_dados_mesa = self.__tela_mesa.pega_dados_mesa()
                mesa.numero = novos_dados_mesa["numero"]
                mesa.capacidade = novos_dados_mesa["capacidade"]
                self.lista_mesas()
            else:
                raise MesaNaoExistenteException(numero_mesa)
        except MesaNaoExistenteException as e:
            self.__tela_mesa.mostra_mensagem(e)

    def lista_mesas(self):
        self.__tela_mesa.mostra_mensagem("------ MESAS ------")
        if len(self.__mesas) == 0:
            self.__tela_mesa.mostra_mensagem("ATENÇÃO: Lista de mesas vazia")
        for mesa in self.__mesas:
            self.__tela_mesa.mostra_dados_mesa({"numero": mesa.numero, "capacidade": mesa.capacidade})
    
    def lista_mesas_disponiveis(self):
        self.__tela_mesa.mostra_mensagem("------MESAS------")
        if len(self.__mesas) == 0:
            self.__tela_mesa.mostra_mensagem("ATENÇÃO: Lista de mesas vazia")
        for mesa in self.__mesas:
            if mesa.status == False:
                self.__tela_mesa.mostra_dados_mesa({"numero": mesa.numero, "capacidade": mesa.capacidade})

    def ha_mesas_disponiveis(self):
        for mesa in self.__mesas:
            if not mesa.status:
                return True
        return False

    def excluir_mesa(self):
        self.lista_mesas()
        numero_mesa = self.__tela_mesa.seleciona_mesa()
        mesa = self.pega_mesa_por_numero(numero_mesa)
        try:
            if(mesa is not None):
                self.__mesas.remove(mesa)
                self.lista_mesas()
            else:
                raise MesaNaoExistenteException(numero_mesa)
        except MesaNaoExistenteException as e:
            self.__tela_mesa.mostra_mensagem(e)
        
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_mesa, 2: self.alterar_mesa, 3: self.excluir_mesa, 4: self.lista_mesas, 5: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_mesa.tela_opcoes()]()
