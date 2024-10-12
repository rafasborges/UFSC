from exceptions.item_nao_existente_exception import ItemNaoExistenteException
from exceptions.pedido_nao_existente_exception import PedidoNaoExistenteException
from exceptions.pedido_repetido_exception import PedidoRepetidoException
from exceptions.reserva_nao_existente_exception import ReservaNaoExistenteException
from limites.tela_pedido import TelaPedido
from entidades.pedido import Pedido

class ControladorPedido():

  def __init__(self, controlador_sistema):
    self.__controlador_sistema = controlador_sistema
    self.__pedidos = []
    self.__total_pedidos = []
    self.__tela_pedido = TelaPedido()

  def pega_pedido_por_codigo(self, codigo: int):
    for pedido in self.__pedidos:
      if(int(pedido.codigo) == int(codigo)):
        return pedido
    return None

  def incluir_pedido(self):
    lista = []
    self.__controlador_sistema.controlador_reservas.lista_reservas()
    self.__tela_pedido.mostra_mensagem("----- CARDÁPIO -----")
    self.__controlador_sistema.controlador_itens_cardapio.lista_itens_cardapio_formatado()

    dados_pedido = self.__tela_pedido.pega_dados_pedido()
    codigo = dados_pedido["codigo"]
    id_reserva = dados_pedido["id_reserva"] 
    lista_itens = dados_pedido["lista_itens"]
    reserva = self.__controlador_sistema.controlador_reservas.pega_reserva_por_id(int(id_reserva))

    try: 
      if reserva is None:
        raise ReservaNaoExistenteException(dados_pedido["id_reserva"] )

      for pedido_existente in self.__pedidos:
        if pedido_existente.codigo == codigo:
            raise PedidoRepetidoException(codigo)
        
      for num in lista_itens:
        item = self.__controlador_sistema.controlador_itens_cardapio.pega_item_por_cod(num)
        if item is None:
          raise ItemNaoExistenteException(num)
        lista.append(item)

      pedido = Pedido(codigo, reserva, lista)
      self.__pedidos.append(pedido)
      self.__total_pedidos.append(pedido)

    except (PedidoRepetidoException, ReservaNaoExistenteException, ItemNaoExistenteException) as e:
        self.__tela_pedido.mostra_mensagem(str(e))
    

  def lista_pedidos(self):
    self.__tela_pedido.mostra_mensagem("------ PEDIDOS ------")
    if len(self.__pedidos) == 0:
       self.__tela_pedido.mostra_mensagem("ATENÇÃO: Lista de pedidos vazia")
    for pedido in self.__pedidos:
        itens_pedido = ""
        for item in pedido.itens:
            if item is not None:
              itens_pedido += "{} - {} - {} - R$ {}\n".format(item.codigo_item, item.nome, item.descricao, item.preco)
            else:
              self.__tela_pedido.mostra_mensagem("Erro! Item é nulo!")
        self.__tela_pedido.mostra_dados_pedido({"codigo": pedido.codigo, "id_reserva": pedido.reserva.id, "itens": itens_pedido})
    
  def excluir_pedido(self):
    self.lista_pedidos()
    codigo = self.__tela_pedido.seleciona_pedido()
    pedido = self.pega_pedido_por_codigo(int(codigo))

    try:
      if (pedido is not None):
        self.__pedidos.remove(pedido)
        self.lista_pedidos()
      else:
        raise PedidoNaoExistenteException(codigo)
    except PedidoNaoExistenteException as e:
      self.__tela_pedido.mostra_mensagem(e)
    

  def pega_pedido_por_id_reserva(self, id_reserva: int):
     lista = []
     for pedido in self.__pedidos:
      if(int(pedido.reserva.id) == int(id_reserva)):
        lista.append(pedido)
     return lista

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_pedido, 2: self.lista_pedidos, 3: self.excluir_pedido, 4: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_pedido.tela_opcoes()]()

  @property
  def total_pedidos(self):
    return self.__total_pedidos
  
  @property
  def pedidos(self):
    return self.__pedidos