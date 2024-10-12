
from controladores.controlador_cliente import ControladorCliente
from controladores.controlador_funcionario import ControladorFuncionario
from controladores.controlador_item_cardapio import ControladorItemCardapio
from controladores.controlador_mesa import ControladorMesa
from controladores.controlador_pedido import ControladorPedido
from controladores.controlador_reserva import ControladorReserva
from limites.tela_sistema import TelaSistema
import PySimpleGUI as sg

class ControladorSistema:

    def __init__(self):
        self.__controlador_mesas = ControladorMesa(self)
        self.__controlador_itens_cardapio = ControladorItemCardapio(self)
        self.__controlador_funcionarios = ControladorFuncionario(self)
        self.__controlador_clientes = ControladorCliente(self)
        self.__controlador_reservas= ControladorReserva(self)
        self.__controlador_pedidos = ControladorPedido(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_mesas(self):
        return self.__controlador_mesas

    @property
    def controlador_itens_cardapio(self):
        return self.__controlador_itens_cardapio

    @property
    def controlador_funcionarios(self):
        return self.__controlador_funcionarios

    @property
    def controlador_clientes(self):
        return self.__controlador_clientes
    
    @property
    def controlador_reservas(self):
        return self.__controlador_reservas

    @property
    def controlador_pedidos(self):
        return self.__controlador_pedidos

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_mesas(self):
        self.__controlador_mesas.abre_tela()

    def cadastra_itens_cardapio(self):
        self.__controlador_itens_cardapio.abre_tela()
    
    def cadastra_funcionarios(self):
        self.__controlador_funcionarios.abre_tela()

    def cadastra_clientes(self):
        self.__controlador_clientes.abre_tela()

    def cadastra_reservas(self):
        self.__controlador_reservas.abre_tela()

    def cadastra_pedidos(self):
        self.__controlador_pedidos.abre_tela()
    
    def encerra_sistema(self):
        exit(0)
    
    def abrir_relatorio_valor_total(self):
        total = 0.0
        total_reservas = self.__controlador_reservas.total_reservas
        total_pedidos = self.__controlador_pedidos.total_pedidos
        for reserva in total_reservas:
            for pedido in total_pedidos:
                if pedido.reserva.id == reserva.id:
                    for item in pedido.itens:
                        total += float(item.preco)

        sg.Popup("O valor ganho total durante o dia com o restaurante foi de R$ {:.2f}".format(total), title = "Total ganho")

    def abrir_relatorio_total_clientes(self):
        total = self.controlador_clientes.calcular_total_clientes()
        sg.Popup("Total de clientes em um dia: {} pessoas.".format(total), title = "Total clientes")
    
    def abrir_relatorio_total_reservas(self):
        total_reservas = self.__controlador_reservas.total_reservas
        total = len(total_reservas)
        sg.Popup("Total de reservas em um dia: {}".format(total), title = "Total reservas")
    
    def abrir_relatorio_mais_pedidos(self):
        contagem_itens = {}
        pedidos = self.__controlador_pedidos.total_pedidos
        for pedido in pedidos:
            for item in pedido.itens:
                if item.nome in contagem_itens:
                    contagem_itens[item.nome] += 1
                else:
                    contagem_itens[item.nome] = 1

        item_mais_pedido = None
        maior_quantidade = 0

        for item, quantidade in contagem_itens.items():
            if quantidade > maior_quantidade:
                maior_quantidade = quantidade
                item_mais_pedido = item

        sg.Popup("Item mais pedido: {}".format(item_mais_pedido))
    
    def finalizar_dia(self):
        self.__controlador_clientes.apagar_clientes()
        self.__controlador_pedidos.apagar_pedidos()
        self.__controlador_pedidos.apagar_total_pedidos()
        self.__controlador_reservas.apagar_reservas()
        self.__controlador_reservas.apagar_total_reservas()
        sg.Popup("---------- DIA FINALIZADO ----------", title = 'FIM')      

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_mesas, 2: self.cadastra_itens_cardapio, 3: self.cadastra_funcionarios,
        4: self.cadastra_clientes, 5: self.cadastra_reservas, 6: self.cadastra_pedidos, 7: self.abrir_relatorio_valor_total, 
        8: self.abrir_relatorio_total_clientes, 9: self.abrir_relatorio_total_reservas, 10: self.abrir_relatorio_mais_pedidos, 11: self.finalizar_dia, 0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()