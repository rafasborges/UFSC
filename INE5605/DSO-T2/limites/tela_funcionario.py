from limites.tela import Tela
import PySimpleGUI as sg

class TelaFuncionario(Tela):
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
        if values['5']:
          opcao = 5
        if button in (None, 'Cancelar', 'Voltar', 'Sair'):
          opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
      sg.ChangeLookAndFeel('TealMono')
      layout = [
        [sg.Text('-------- FUNCIONÁRIOS ----------', font=("Helvica", 25))],
        [sg.Text('Escolha sua opção', font=("Helvica", 15))],
        [sg.Radio('Incluir Funcionário', "RD1", key='1')],
        [sg.Radio('Alterar Funcionário', "RD1", key='2')],
        [sg.Radio('Excluir Funcionário', "RD1", key='3')],
        [sg.Radio('Listar Funcionário', "RD1", key='4')],
        [sg.Radio('Ver salário Funcionário', "RD1", key='5')],
        [sg.Cancel('Voltar'), sg.Button('Confirmar')]
      ]
      self.__window = sg.Window('Sistema de Restaurante').Layout(layout)

    def pega_dados_funcionario(self):
        sg.ChangeLookAndFeel('TealMono')
        while True:
            try:
                layout = [
                [sg.Text('-------- DADOS FUNCIONÁRIOS ----------', font=("Helvica", 25))],
                [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
                [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
                [sg.Text('Salário:', size=(15, 1)), sg.InputText('', key='salario')],
                [sg.Cancel('Voltar'), sg.Button('Confirmar')]
              ]
                self.__window = sg.Window('Sistema de Restaurante').Layout(layout)

                button, values = self.open()
                if button in [sg.WIN_CLOSED, 'Voltar']:
                    self.__window.close()
                    return None
                nome = str(values['nome'])

                cpf = str(values['cpf'])
                salario = float(values['salario'])

                if ((self.checa_valor(nome) == True) or
                        (not isinstance(salario, (int, float)) or
                        len(cpf) != 11) or
                        salario < 0):
                        raise ValueError
                self.close()
                return {"nome": nome.upper(), "cpf": cpf, "salario": salario}
            except ValueError:
                sg.Popup("Dados incorretos! O CPF deve conter 11 dígitos! Utilize apenas strings para o nome e números decimais positivos para o salário!", title = "ERRO")
            self.close()

    def mostra_funcionario(self, dados_funcionario):
        try:
            string_todos_funcionarios = ""
            for dado in dados_funcionario:
                string_todos_funcionarios = string_todos_funcionarios + "NOME DO FUNCIONARIO: " + str(dado["nome"]) + '\n'
                string_todos_funcionarios = string_todos_funcionarios + "CPF DO FUNCIONARIO: " + str(dado["cpf"]) + '\n'
                string_todos_funcionarios = string_todos_funcionarios + "SALÁRIO DO FUNCIONARIO: " + str(dado["salario"]) + '\n\n'

            sg.Popup('-------- LISTA DE FUNCIONÁRIOS ----------', string_todos_funcionarios, title='')
        except KeyError as e:
            sg.Popup("Erro ao exibir dados de funcionários: ", str(e))


    def seleciona_funcionario(self):
      sg.ChangeLookAndFeel('TealMono')

      while True:
        try:
          layout = [
            [sg.Text('-------- SELECIONAR FUNCIONÁRIO ----------', font=("Helvica", 25))],
            [sg.Text('Digite o nome do funcionario que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Cancel('Voltar'), sg.Button('Confirmar')]
          ]
          self.__window = sg.Window('Seleciona funcionário').Layout(layout)

          button, values = self.open()
          if button in [sg.WIN_CLOSED, 'Voltar']:
                    self.__window.close()
                    return None

          nome = str(values['nome'])

          if not isinstance(nome, str):
            raise ValueError
          self.close()
          return nome.upper()

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
