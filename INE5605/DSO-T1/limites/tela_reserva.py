from limites.tela import Tela


class TelaReserva(Tela):

  def tela_opcoes(self):
    print("-------- RESERVA ----------")
    print("Escolha a opcao")
    print("1 - Adicionar Reserva")
    print("2 - Listar Reservas")
    print("3 - Excluir Reserva")
    print("4 - Calcular valor total de uma Reserva")
    print("5 - Voltar")
    opcao = self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4, 5])
    return opcao

  def pega_dados_reserva(self):
    print("-------- DADOS RESERVA ----------")
    while True:
      try:
        id = int(input("Id da Reserva: "))
        mesa_num = int(input("Número da Mesa: "))
        cliente_cpf = str(input("CPF do cliente: "))
        funcionario_nome = str(input("Nome do funcionário: "))
        if ((not isinstance(id, int)) or 
            (not isinstance(mesa_num, int)) or
             (self.checa_valor(funcionario_nome) == True)
             or len(cliente_cpf) != 11):
          raise ValueError
        return {"id": id, "mesa_num": mesa_num, "cliente_cpf": cliente_cpf, "funcionario_nome": funcionario_nome.upper()}
      except ValueError:
        print("Dados incorretos! O CPF deve conter 11 dígitos! Utilize apenas inteiros para o id e número da mesa e string para o nome do funcionário!")
  

  def mostra_reserva(self, dados_reserva):
    try:
      print("Id da reserva: ", dados_reserva["id_reserva"])
      print("Nome do Cliente: ", dados_reserva["nome_cliente"])
      print("Nome do funcionário responsável: ", dados_reserva["nome_funcionario"].upper())
      print("Número da Mesa: ", dados_reserva["num_mesa"])
      print("\n")
    except KeyError as e:
      print("Erro ao exibir dados da reserva: ", str(e))
      print("\n")

  def seleciona_reserva(self):
    while True:
      id = input("Id da reserva que deseja selecionar: ")
      try:
        id = int(id)
        if not isinstance(id, int):
          raise ValueError
        return id
      except ValueError:
        print("\nInsira um valor válido! O número da reserva deve ser um valor inteiro!")
        print("\n")

  def mostra_ganho_reserva(self, id_reserva, total):
    print("Valor total da reserva {}: {}".format(id_reserva, total))

 