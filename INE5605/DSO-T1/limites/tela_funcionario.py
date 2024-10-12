from limites.tela import Tela


class TelaFuncionario(Tela):

    def tela_opcoes(self):
        print("--------- CADASTRO FUNCIONÁRIO --------- ")
        print(" 1 - Incluir Funcionário")
        print(" 2 - Alterar Funcionário")
        print(" 3 - Excluir Funcionário")
        print(" 4 - Listar Funcionário")
        print(" 5 - Ver salário Funcionário")
        print(" 6 - Voltar")
        opcao = self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4, 5, 6])
        return opcao

    def pega_dados_funcionario(self):
        print("-------- DADOS FUNCIONARIO ----------")
        while True:
            try:
                nome = input("Nome: ")
                cpf = input("CPF: ")
                salario = float(input("Salário: "))
                if ((self.checa_valor(nome) == True) or
                    (not isinstance(salario, (int, float)) or
                    len(cpf) != 11) or
                    salario < 0):
                    raise ValueError
                return {"nome": nome.upper(), "cpf": cpf, "salario": salario}
            except ValueError:
                print("Dados incorretos! O CPF deve conter 11 dígitos! Utilize apenas strings para o nome e números decimais positivos para o salário!")
    

    def mostra_funcionario(self, dados_funcionario):
        try:
            print("NOME DO FUNCIONARIO: ", dados_funcionario["nome"].upper())
            print("CPF DO FUNCIONARIO: ", dados_funcionario["cpf"])
            print("SALÁRIO DO FUNCIONARIO: ", dados_funcionario["salario"])
        except KeyError as e:
            print("Erro ao exibir dados do funcionário:", str(e))
        print("\n")

    def seleciona_funcionario(self):
        while True:
            nome_lido = input("Nome do funcionario que deseja selecionar: ").upper()
            try:
                nome = str(nome_lido)
                if not isinstance(nome, str):
                    raise ValueError
                return nome
            except ValueError:
                print("\nInsira um valor válido!")
                print("\n")

