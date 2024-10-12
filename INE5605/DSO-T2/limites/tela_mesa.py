from limites.tela import Tela
import PySimpleGUI as sg


class TelaMesa(Tela):
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
            [sg.Text('-------- MESAS ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir Mesa', "RD1", key='1')],
            [sg.Radio('Alterar Mesa', "RD1", key='2')],
            [sg.Radio('Excluir Mesa', "RD1", key='3')],
            [sg.Radio('Listar Mesa', "RD1", key='4')],
            [sg.Cancel('Voltar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window('Sistema de Restaurante').Layout(layout)

    def pega_dados_mesa(self):
        sg.ChangeLookAndFeel('TealMono')
        while True:
            try:
                layout = [
                    [sg.Text('-------- DADOS MESA ----------', font=("Helvica", 25))],
                    [sg.Text('Número:', size=(15, 1)), sg.InputText('', key='numero')],
                    [sg.Text('Capacidade:', size=(15, 1)), sg.InputText('', key='capacidade')],
                    [sg.Cancel('Voltar'), sg.Button('Confirmar')]
                ]
                self.__window = sg.Window('Sistema de Restaurante').Layout(layout)

                button, values = self.open()
                if button in [sg.WIN_CLOSED, 'Voltar']:
                    self.__window.close()
                    return None

                numero = int(values['numero'])
                capacidade = int(values['capacidade'])

                if ((not isinstance(numero, int) or
                        not isinstance(capacidade, int) or
                        numero < 0 or capacidade < 0)):
                        raise ValueError
                self.close()
                return {"numero": numero, "capacidade": capacidade}

            except ValueError:
                    sg.Popup("Dados incorretos, utilize apenas números positivos para número e capacidade!", title = "ERRO")
                    self.close()

    def mostra_dados_mesa(self, dados_mesa):
        sg.ChangeLookAndFeel('TealMono')

        try:
            string_todas_mesas = ""
            for mesa in dados_mesa:
                string_todas_mesas = string_todas_mesas + "NÚMERO DA MESA: " + str(mesa["numero"]) + '\n'
                string_todas_mesas = string_todas_mesas + "CAPACIDADE DA MESA: " + str(mesa["capacidade"]) + '\n\n'

            sg.Popup('-------- LISTA DE MESAS ----------', string_todas_mesas, title='')
        except KeyError as e:
            sg.Popup("Erro ao exibir dados da mesa: ", str(e))



    def seleciona_mesa(self):
        sg.ChangeLookAndFeel('TealMono')

        while True:
            try:
                layout = [
                    [sg.Text('-------- SELECIONAR MESA ----------', font=("Helvica", 25))],
                    [sg.Text('Digite o número da mesa que deseja selecionar:', font=("Helvica", 15))],
                    [sg.Text('Número:', size=(15, 1)), sg.InputText('', key='numero')],
                    [sg.Button('Voltar'), sg.Cancel('Confirmar')]
                ]
                self.__window = sg.Window('Seleciona mesa').Layout(layout)

                button, values = self.open()
                if button in [sg.WIN_CLOSED, 'Voltar']:
                    self.__window.close()
                    return None
 
                num_mesa = int(values['numero'])

                if (not isinstance(num_mesa, int) or (num_mesa < 0)):
                    raise ValueError
                self.close()
                return num_mesa

            except ValueError:
                sg.Popup("Insira um valor válido! O número da mesa deve ser um valor inteiro!", title = "ERRO")
                self.close()

    def mostra_mensagem(self, msg):
        sg.popup("", msg, title='')

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
