from limites.tela import Tela


class TelaItemCardapio(Tela):

  def tela_opcoes(self):
    print("-------- Itens Cardápio ----------")
    print("Escolha a opcao")
    print("1 - Incluir Item")
    print("2 - Alterar Item")
    print("3 - Excluir Item")
    print("4 - Listar Itens")
    print("5 - Voltar")

    opcao = self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4, 5])
    return opcao

  def pega_dados_item_cardapio(self):
    print("-------- DADOS ITEM CARDÁPIO ----------")
    while True:
        try:
          nome = input("Nome: ")
          descricao = input("Descrição: ")
          codigo_item = int(input("Código: "))
          preco = float(input("Preço: "))
          if ((self.checa_valor(nome) == True) or
                  (self.checa_valor(descricao) == True) or
                  not isinstance(codigo_item, int) or
                  not isinstance(preco, float)):
             raise ValueError
          return {"nome": nome.upper(), "descricao": descricao.upper(), "codigo_item": codigo_item, "preco": preco}
        except ValueError:
          print("Dados incorretos, utilize apenas números positivos em código e preço e letras em nome e descrição!")
    
  def mostra_item_cardapio(self, dados_item):
    try:
        print("NOME DO ITEM: ", dados_item["nome"])
        print("DESCRIÇÃO DO ITEM: ", dados_item["descricao"])
        print("CÓDIGO DO ITEM: ", dados_item["codigo_item"])
        print("PREÇO DO ITEM: ", dados_item["preco"])
    except KeyError as e:
        print("Erro ao exibir dados do item do cardápio:", str(e))
    print("\n")


  def mostra_item_cardapio_formatado(self, dados_item):
   print("{} - {} - {} - R$ {:.2f}".format(dados_item["codigo_item"], dados_item["nome"], dados_item["descricao"], float(dados_item["preco"])))
        

  def seleciona_item(self):
    while True:
      codigo_item = input("Código do item que deseja selecionar: ")
      try:
        codigo_item = int(codigo_item)
        if not isinstance(codigo_item, int):
          raise ValueError
        return codigo_item
      except ValueError:
        print("\nCódigo do item inválido. O código deve ser um valor inteiro.")
        print("\n")
    
