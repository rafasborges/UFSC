from entidades.cliente import Cliente
from exceptions.cliente_de_menor_exception import ClienteDeMenorException
from exceptions.cliente_nao_existente_exception import ClienteNaoExistenteException
from exceptions.cliente_repetido_exception import ClienteRepetidoException
from limites.tela_cliente import TelaCliente


class ControladorCliente():

    def __init__(self, controlador_sistema):
        self.__clientes = []
        self.__tela_cliente = TelaCliente()
        self.__controlador_sistema = controlador_sistema
    
    def verificar_maioridade(self, idade: int):
        if idade >= 18:
            return True
    
    def calcular_total_clientes(self):
        pessoas = 0
        for cliente in self.__clientes:
            pessoas += 1 + int(cliente.num_convidados)
        return pessoas

    def pega_cliente_por_cpf(self, cpf: str):
        for cliente in self.__clientes:
            if(cliente.cpf == str(cpf)):
                return cliente
        return None

    def incluir_cliente(self):
        dados_cliente = self.__tela_cliente.pega_dados_cliente()
        cpf = dados_cliente["cpf"]
        cliente = self.pega_cliente_por_cpf(cpf)
        idade = int(dados_cliente["idade"])
        i = self.verificar_maioridade(idade)
        try:
            if i:
                try:
                    if cliente == None:
                        cliente = Cliente(dados_cliente["nome"], dados_cliente["cpf"], dados_cliente["idade"], dados_cliente["num_convidados"])
                        self.__clientes.append(cliente)
                    else:
                        raise ClienteRepetidoException(cpf)
                except ClienteRepetidoException as e:
                    self.__tela_cliente.mostra_mensagem(e)
            else:
                raise ClienteDeMenorException(idade)
        except ClienteDeMenorException as a:
            self.__tela_cliente.mostra_mensagem(a)

    def alterar_cliente(self):
        self.lista_clientes()
        cpf_cliente = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_cpf(cpf_cliente)

        try:
            if(cliente is not None):
                novos_dados_cliente = self.__tela_cliente.pega_dados_cliente()
                cliente.nome = novos_dados_cliente["nome"]
                cliente.cpf = novos_dados_cliente["cpf"]
                cliente.idade = novos_dados_cliente["idade"]
                cliente.num_convidados = novos_dados_cliente["num_convidados"]
                self.lista_clientes()
            else:
                raise ClienteNaoExistenteException(cpf_cliente)
        except ClienteNaoExistenteException as e:
            self.__tela_cliente.mostra_mensagem(e)


    def lista_clientes(self):
        self.__tela_cliente.mostra_mensagem("----- CLIENTES ------")
        if len(self.__clientes) == 0:
                self.__tela_cliente.mostra_mensagem("ATENÇÃO: Lista de clientes vazia")
        for cliente in self.__clientes:
            self.__tela_cliente.mostra_cliente({"nome": cliente.nome, "cpf": cliente.cpf, "idade": cliente.idade, "num_convidados": cliente.num_convidados})

    def excluir_cliente(self):
        self.lista_clientes()
        cpf_cliente = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_cpf(cpf_cliente)

        try:
            if cliente is not None:
                self.__clientes.remove(cliente)
                self.lista_clientes()
            else:
                raise ClienteNaoExistenteException(cpf_cliente)
        except ClienteNaoExistenteException as e:
            self.__tela_cliente.mostra_mensagem(e)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_cliente, 2: self.alterar_cliente, 3: self.lista_clientes, 4: self.excluir_cliente, 5: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_cliente.tela_opcoes()]()

    @property
    def clientes(self):
        return self.__clientes