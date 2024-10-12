from limites.tela import Tela


class TelaSistema(Tela):

    def tela_opcoes(self):
        print(" ===================================")
        print("|       SISTEMA RESTAURANTE         |")
        print(" ===================================")
        print("------------ RESTAURANTE ------------")
        print("1 - Mesas")
        print("2 - Itens do cardápio")
        print("3 - Funcionários")
        print("-------------- SISTEMA --------------")
        print("4 - Clientes")
        print("5 - Reservas")
        print("6 - Pedidos")
        print("------------ RELATÓRIOS -------------")
        print("7 - Relatório Valor Total")
        print("8 - Relatório Total Clientes")
        print("9 - Relatório Total Reservas")
        print("10 - Relatório Mais Pedidos")
        print("-------------------------------------")
        print("11 - Finalizar o dia")
        print("0 - Finalizar sistema")
        print("-------------------------------------")
        opcao = self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
        return opcao

