from limites.tela import Tela
from limites.tela_sistema import TelaSistema


class TelaMesa(Tela):

    def tela_opcoes(self):
        print("--------- CADASTRO MESAS --------- ")
        print(" 1 - Incluir Mesa")
        print(" 2 - Alterar Mesa")
        print(" 3 - Excluir Mesa")
        print(" 4 - Listar Mesas")
        print(" 5 - Voltar")
        opcao = self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4, 5])
        return opcao
       

    def pega_dados_mesa(self):
        print("-------- DADOS MESA ----------")
        while True:
            try:
                numero = int(input("Número: "))
                capacidade = int(input("Capacidade: "))
                if (not isinstance(numero, int) or
                    not isinstance(capacidade, int) or
                    numero < 0 or capacidade < 0):
                    raise ValueError
                return {"numero": numero, "capacidade": capacidade}
            except ValueError:
                print("Dados incorretos, utilize apenas números positivos para número e capacidade!")


    def mostra_dados_mesa(self, dados_mesa):
        try:
            print("NÚMERO DA MESA: ", dados_mesa["numero"])
            print("CAPACIDADE DA MESA: ", dados_mesa["capacidade"])
        except KeyError as e:
            print("Erro ao exibir dados da mesa: ", str(e))
        print("\n")


    def seleciona_mesa(self):
        while True:
            numero = input("Número da mesa que deseja selecionar: ")
            try:
                numero = int(numero)
                if not isinstance(numero, int):
                    raise ValueError
                return numero
            except ValueError:
                print("\nInsira um valor válido! O número da mesa deve ser um valor inteiro!")
                print("\n")


