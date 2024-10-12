from limites.tela import Tela
import PySimpleGUI as sg

class TelaSistema(Tela):
    def __init__(self):
        self.__window = None
        self.init_components()

    def tela_opcoes(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['5']:
            opcao = 5
        if values['6']:
            opcao = 6
        if values['7']:
            opcao = 7
        if values['8']:
            opcao = 8
        if values['9']:
            opcao = 9
        if values['10']:
            opcao = 10
        if values['11']:
            opcao = 11
        if values['0'] or button in (None, 'Cancelar', 'Voltar', 'Sair'):
            opcao = 0
        self.close()
        return opcao

    def close(self):
        self.__window.Close()

    def init_components(self):
        sg.ChangeLookAndFeel('TealMono')
        layout = [
            [sg.Text('Bem vindo ao Sistema de Restaurante!', font=("Helvica",25))],
            [sg.Text('ESCOLHA SUA OPÇÃO:', font=("Helvica",15)), sg.T(""), sg.T(""), sg.T(""), sg.T(""), sg.T(""), sg.T(""), sg.T(""), sg.Text('RELATÓRIOS', font=("Helvica",15))],
            [sg.Radio('Mesas',"RD1", key='1'), sg.Text(" " * 60), sg.Radio('Relatório Valor Total',"RD1", key='7')],
            [sg.Radio('Itens do cardápio',"RD1", key='2'), sg.Text(" " * 45), sg.Radio('Relatório Total Clientes',"RD1", key='8')],
            [sg.Radio('Funcionários',"RD1", key='3'), sg.Text(" " * 51), sg.Radio('Relatório Total Reservas',"RD1", key='9')],
            [sg.Radio('Clientes',"RD1", key='4'), sg.Text(" " * 58), sg.Radio('Relatório Mais Pedidos',"RD1", key='10')],
            [sg.Radio('Reservas',"RD1", key='5')],
            [sg.Radio('Pedidos',"RD1", key='6')],
            [sg.Text('ENCERRAR', font=("Helvica",15))],
            [sg.Radio('Finalizar o dia',"RD1", key='11')],
            [sg.Radio('Finalizar sistema',"RD1", key='0')],
            [sg.Cancel('Cancelar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window('Sistema de Restaurante').Layout(layout)