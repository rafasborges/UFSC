from limites.tela import Tela
import PySimpleGUI as sg


class TelaPedido(Tela):
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
        if button in (None, 'Cancelar', 'Voltar', 'Sair'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('TealMono')
        layout = [
            [sg.Text('-------- PEDIDOS ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir Pedido', "RD1", key='1')],
            [sg.Radio('Listar Pedido', "RD1", key='2')],
            [sg.Radio('Excluir Pedido', "RD1", key='3')],
            [sg.Cancel('Voltar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window('Sistema de Restaurante').Layout(layout)

    def pega_dados_pedido(self):
        sg.ChangeLookAndFeel('TealMono')
        while True:
            try:
                layout = [
                    [sg.Text('-------- DADOS PEDIDO ----------', font=("Helvica", 25))],
                    [sg.Text('Código do Pedido:', size=(15, 1)), sg.InputText('', key='codigo', size=(51, 1))],
                    [sg.Text('Id da Reserva que efetuou o Pedido:', size=(26, 1)), sg.InputText('', key='id_reserva', size=(38, 1))],
                    [sg.Text('Código dos itens que deseja selecionar (separados por vírgula):', size=(46, 1)), sg.InputText('', key='cod_itens', size=(15, 1))],
                    [sg.Cancel('Voltar'), sg.Button('Confirmar')]
                ]
                self.__window = sg.Window('Sistema de Restaurante').Layout(layout)

                button, values = self.open()
                if button in [sg.WIN_CLOSED, 'Voltar']:
                    self.__window.close()
                    return None

                codigo = int(values['codigo'])
                id_reserva = int(values['id_reserva'])
                cod_itens = values['cod_itens']
                lista_itens = [int(numero) for numero in cod_itens.split(",")]
                    
                if button != 'Voltar' and ((not isinstance(codigo, int)) or
                                            (not isinstance(id_reserva, int))):
                    raise ValueError
                self.close()
                return {"codigo": codigo, "id_reserva": id_reserva, "lista_itens": lista_itens}
            
            except ValueError:
                    sg.Popup("Dados incorretos! Utilize apenas inteiros para o código e id da reserva!", title = "ERRO")
                    self.close()

    def mostra_dados_pedido(self, dados_pedido):
        try:
            string_todos_pedidos = ""
            for pedido in dados_pedido:
                print(pedido)
                string_todos_pedidos += "CÓDIGO DO PEDIDO: " + str(pedido["codigo"]) + '\n'
                string_todos_pedidos += "ID DA RESERVA: " + str(pedido["id_reserva"]) + '\n'
                string_todos_pedidos += "ITENS DO PEDIDO: " + '\n' + str(pedido["itens"]) + '\n\n'

            sg.Popup('-------- LISTA DE PEDIDOS ----------', string_todos_pedidos, title='')
        except KeyError as e:
            sg.Popup("Erro ao exibir dados do pedido: ", str(e))

    def seleciona_pedido(self):
        sg.ChangeLookAndFeel('TealMono')
        while True:
            try:
                layout = [
                    [sg.Text('-------- SELECIONAR PEDIDO ----------', font=("Helvica", 25))],
                    [sg.Text('Digite o código do pedido que deseja selecionar:', font=("Helvica", 15))],
                    [sg.Text('Código:', size=(15, 1)), sg.InputText('', key='codigo')],
                    [sg.Button('Voltar'), sg.Cancel('Confirmar')]
                ]
                self.__window = sg.Window('Seleciona pedido').Layout(layout)

                button, values = self.open()
                if button in [sg.WIN_CLOSED, 'Voltar']:
                    self.__window.close()
                    return None

                codigo = int(values['codigo'])
                if not isinstance(codigo, int):
                    raise ValueError
                self.close()
                return codigo
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