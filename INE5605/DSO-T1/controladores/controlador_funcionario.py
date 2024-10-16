from entidades.funcionario import Funcionario
from exceptions.funcionario_nao_existente_exception import FuncionarioNaoExistenteException
from exceptions.funcionario_repetido_exception import FuncionarioRepetidoException
from limites.tela_funcionario import TelaFuncionario

class ControladorFuncionario():
    def __init__(self, controlador_sistema):
        self.__funcionarios = []
        self.__tela_funcionario = TelaFuncionario()
        self.__controlador_sistema = controlador_sistema

    def pega_funcionario_por_nome(self, nome: str):
        for funcionario in self.__funcionarios:
            if(funcionario.nome == nome):
                return funcionario
        return None

    def pega_funcionario_por_cpf(self, cpf: str):
        for funcionario in self.__funcionarios:
            if(funcionario.cpf == cpf):
                return funcionario
        return None

    def incluir_funcionario(self):
        dados_funcionario = self.__tela_funcionario.pega_dados_funcionario()
        cpf = dados_funcionario["cpf"]
        funcionario = self.pega_funcionario_por_cpf(cpf)
        try:
            if funcionario == None:
                funcionario = Funcionario(dados_funcionario["nome"], dados_funcionario["cpf"], dados_funcionario["salario"])
                self.__funcionarios.append(funcionario)
            else:
                raise FuncionarioRepetidoException(cpf)
        except FuncionarioRepetidoException as e:
            self.__tela_funcionario.mostra_mensagem(e)


    def alterar_funcionario(self):
        self.lista_funcionarios()
        nome_funcionario = self.__tela_funcionario.seleciona_funcionario()
        funcionario = self.pega_funcionario_por_nome(nome_funcionario)

        try:    
            if(funcionario is not None):
                novos_dados_funcionario = self.__tela_funcionario.pega_dados_funcionario()
                funcionario.nome = novos_dados_funcionario["nome"]
                funcionario.cpf = novos_dados_funcionario["cpf"]
                funcionario.idade = novos_dados_funcionario["salario"]
                self.lista_funcionarios()
            else:
                raise FuncionarioNaoExistenteException(nome_funcionario)
        except FuncionarioNaoExistenteException as a:
            self.__tela_funcionario.mostra_mensagem(a)


    def lista_funcionarios(self):
        self.__tela_funcionario.mostra_mensagem("----- FUNCIONÁRIOS ------")
        if len(self.__funcionarios) == 0:
                self.__tela_funcionario.mostra_mensagem("ATENÇÃO: Lista de funcionários vazia")
        for funcionario in self.__funcionarios:
            self.__tela_funcionario.mostra_funcionario({"nome": funcionario.nome, "cpf": funcionario.cpf, "salario": funcionario.salario})

    def excluir_funcionario(self):
        self.lista_funcionarios()
        nome_funcionario = self.__tela_funcionario.seleciona_funcionario()
        funcionario = self.pega_funcionario_por_nome(nome_funcionario)
        
        try:
            if(funcionario is not None):
                self.__funcionarios.remove(funcionario)
                self.lista_funcionarios()
            else:
                raise FuncionarioNaoExistenteException(nome_funcionario)
        except FuncionarioNaoExistenteException as a:
            self.__tela_funcionario.mostra_mensagem(a)
        
    def calcular_salario(self):
        self.lista_funcionarios()
        nome_funcionario = self.__tela_funcionario.seleciona_funcionario()
        funcionario = self.pega_funcionario_por_nome(nome_funcionario)

        total = 0.0

        lista_reservas = self.__controlador_sistema.controlador_reservas.total_reservas
        for reserva in lista_reservas:
            if reserva.funcionario.nome == nome_funcionario:
                pedidos = self.__controlador_sistema.controlador_pedidos.pega_pedido_por_id_reserva(int(reserva.id))
                for pedido in pedidos:
                    for item in pedido.itens:
                        total += float(item.preco)

        comissao = 0.1 * total
        sal = float(funcionario.salario) + float(comissao)
        self.__tela_funcionario.mostra_mensagem("A comissão do funcionário {} foi de R$ {:.2f}. O salário total do funcionário é R$ {}".format(funcionario.nome, comissao, sal))


    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_funcionario, 2: self.alterar_funcionario, 3: self.excluir_funcionario, 4: self.lista_funcionarios, 5:self.calcular_salario, 6:self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_funcionario.tela_opcoes()]()