from limites.tela import Tela


class TelaCliente(Tela):
                    
    def tela_opcoes(self):
        print("--------- CADASTRO CLIENTE --------- ")
        print(" 1 - Incluir Cliente")
        print(" 2 - Alterar Cliente")
        print(" 3 - Listar Clientes")
        print(" 4 - Excluir Cliente")
        print(" 5 - Voltar")
        opcao = self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4, 5])
        return opcao
    
    def pega_dados_cliente(self):
        print("-------- DADOS CLIENTE ----------")
        while True:
            try:
                nome = input("Nome: ")
                cpf = input("CPF: ")
                num_convidados = int(input("Número de convidados: "))
                idade = int(input("Idade: "))
                if ((self.checa_valor(nome) == True) or
                    len(cpf) != 11 or
                    (not isinstance(num_convidados, int)) or
                     (not isinstance(idade, int))):
                    raise ValueError
                return {"nome": nome, "cpf": cpf, "num_convidados": num_convidados, "idade": idade}
            except ValueError:
                print("Dados incorretos! O CPF deve conter 11 dígitos! Utilize apenas strings para o nome e números inteiros para a idade e número de convidados!")
            
    def mostra_cliente(self, dados_cliente):
        try:
            print("NOME DO CLIENTE: ", dados_cliente["nome"])
            print("CPF DO CLIENTE: ", dados_cliente["cpf"])
            print("IDADE DO CLIENTE: ", dados_cliente["idade"])
            print("NÚMERO DE CONVIDADOS DO CLIENTE: ", dados_cliente["num_convidados"])
        except KeyError as e:
            print("Erro ao exibir dados do cliente:", str(e))
        print("\n")


    def seleciona_cliente(self):        
        while True:
            cpf_lido = input("CPF do cliente que deseja selecionar: ")
            try:
                cpf = str(cpf_lido)
                if not isinstance(cpf, str):
                    raise ValueError
                return cpf
            except ValueError:
                print("\nInsira um valor válido!")
                print("\n")

