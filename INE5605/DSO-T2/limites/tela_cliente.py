import PySimpleGUI as sg
from limites.tela import Tela

class TelaCliente(Tela):
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        # opcao = 0
        if values['1']:
          opcao = 1
        if values['2']:
          opcao = 2
        if values['3']:
          opcao = 3
        if values['4']:
          opcao = 4
        if button in (None, 'Cancelar', 'Voltar', 'Sair'):
          opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
      sg.ChangeLookAndFeel('TealMono')
      layout = [
        [sg.Text('-------- CLIENTES ----------', font=("Helvica", 25))],
        [sg.Text('Escolha sua opção', font=("Helvica", 15))],
        [sg.Radio('Incluir Cliente', "RD1", key='1')],
        [sg.Radio('Alterar Cliente', "RD1", key='2')],
        [sg.Radio('Listar Cliente', "RD1", key='3')],
        [sg.Radio('Excluir Cliente', "RD1", key='4')],
        [sg.Cancel('Voltar'), sg.Button('Confirmar')]
      ]
      self.__window = sg.Window('Sistema de Restaurante').Layout(layout)

    def pega_dados_cliente(self):
        sg.ChangeLookAndFeel('TealMono')
        while True:
            try:
                layout = [
                    [sg.Text('-------- DADOS CLIENTE ----------', font=("Helvica", 25))],
                    [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
                    [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
                    [sg.Text('N. de convidados:', size=(15, 1)), sg.InputText('', key='num_convidados')],
                    [sg.Text('Idade:', size=(15, 1)), sg.InputText('', key='idade')],
                    [sg.Cancel('Voltar'), sg.Button('Confirmar')]
                ]
                self.__window = sg.Window('Sistema de Restaurante').Layout(layout)

                button, values = self.open()
                if button in [sg.WIN_CLOSED, 'Voltar']:
                    self.__window.close()
                    return None

                nome = str(values['nome'])
                cpf = str(values['cpf'])
                num_convidados = int(values['num_convidados'])
                idade = int(values['idade'])

                if ((self.checa_valor(nome) == True) or len(cpf) != 11 or (not isinstance(num_convidados, int)) or (not isinstance(idade, int))):
                    raise ValueError
                self.close()
                return {"nome": nome.upper(), "cpf": cpf, "num_convidados": num_convidados, "idade": idade}
            except ValueError:
                    sg.Popup("Dados incorretos! O CPF deve conter 11 dígitos! Utilize apenas strings para o nome e números inteiros para a idade e número de convidados!", title = "ERRO")
                    self.close()

    def mostra_cliente(self, dados_cliente):
        sg.ChangeLookAndFeel('TealMono')
        try:
            string_todos_clientes = ""
            for dado in dados_cliente:
                string_todos_clientes = string_todos_clientes + "NOME DO CLIENTE: " + str(dado["nome"]) + '\n'
                string_todos_clientes = string_todos_clientes + "CPF DO CLIENTE: " + str(dado["cpf"]) + '\n'
                string_todos_clientes = string_todos_clientes + "NUM. DE CONVIDADOS: " + str(dado["num_convidados"]) + '\n'
                string_todos_clientes = string_todos_clientes + "IDADE: " + str(dado["idade"]) + '\n\n'

            sg.Popup('-------- LISTA DE CLIENTES ----------', string_todos_clientes, title='')

        except KeyError as e:
            sg.Popup("Erro ao exibir dados do cliente: ", str(e))

    def seleciona_cliente(self):
        sg.ChangeLookAndFeel('TealMono')
        while True:
            try:
                layout = [
                    [sg.Text('-------- SELECIONAR CLIENTE ----------', font=("Helvica", 25))],
                    [sg.Text('Digite o CPF do cliente que deseja selecionar:', font=("Helvica", 15))],
                    [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
                    [sg.Cancel('Voltar'), sg.Button('Confirmar')]
                ]
                self.__window = sg.Window('Seleciona cliente').Layout(layout)

                button, values = self.open()
                if button in [sg.WIN_CLOSED, 'Voltar']:
                    self.__window.close()
                    return None
                cpf = str(values['cpf'])
                if not isinstance(cpf, str):
                    raise ValueError
                self.close()
                return cpf
            except ValueError:
                sg.Popup("Insira um valor válido!", title = "ERRO")
                self.close()

    def mostra_mensagem(self, msg):
        sg.popup("", msg, title='')

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values