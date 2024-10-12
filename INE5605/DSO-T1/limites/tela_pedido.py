from limites.tela import Tela


class TelaPedido(Tela):

    def tela_opcoes(self):
        print("--------- CADASTRO PEDIDO --------- ")
        print(" 1 - Incluir Pedido")
        print(" 2 - Listar Pedidos")
        print(" 3 - Excluir Pedido")
        print(" 4 - Voltar")
        opcao = self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4, 5, 6])
        return opcao
    

    def pega_dados_pedido(self):
        print("-------- DADOS PEDIDO ----------")
        while True:
            try:
                codigo = int(input("Código do Pedido: "))
                id_reserva = int(input("Id da Reserva que efetuou o Pedido: "))
                cod_itens= input("Código dos itens que deseja selecionar (separados por vírgula): ")
                lista_itens = [int(numero) for numero in cod_itens.split(",")]
                if ((not isinstance(codigo, int)) or
                    (not isinstance(id_reserva, int))):
                    raise ValueError
                return {"codigo": codigo, "id_reserva": id_reserva, "lista_itens": lista_itens}
            except ValueError:
                    print("Dados incorretos! Utilize apenas inteiros para o código e id da reserva!")


    def mostra_dados_pedido(self, dados_pedido):
        try:
            print("Código: ", dados_pedido["codigo"])
            print("Id da reserva: ", dados_pedido["id_reserva"])
            print("Itens: ", dados_pedido["itens"])
            print("\n")
        except KeyError as e:
            print("Erro ao exibir dados do pedido: ", str(e))
            print("\n")

    def seleciona_pedido(self):
        while True:
            codigo = input("Código do item que deseja selecionar: ")
            try:
                codigo = int(codigo)
                if not isinstance(codigo, int):
                    raise ValueError
                return codigo
            except ValueError:
                print("\nCódigo do item inválido. O código deve ser um valor inteiro.")
                print("\n") 

