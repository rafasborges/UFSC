from DAOs.pedido_dao import PedidoDAO
from exceptions.item_nao_existente_exception import ItemNaoExistenteException
from exceptions.pedido_nao_existente_exception import PedidoNaoExistenteException
from exceptions.pedido_repetido_exception import PedidoRepetidoException
from exceptions.reserva_nao_existente_exception import ReservaNaoExistenteException
from limites.tela_pedido import TelaPedido
from entidades.pedido import Pedido

class ControladorPedido():
  def __init__(self, controlador_sistema):
    self.__controlador_sistema = controlador_sistema
    self.__pedido_DAO= PedidoDAO()
    self.__total_pedidos = PedidoDAO()
    self.__tela_pedido = TelaPedido()

  def pega_pedido_por_codigo(self, codigo: int):
    for pedido in self.__pedido_DAO.get_all():
      if(int(pedido.codigo) == int(codigo)):
        return pedido
    return None

  def incluir_pedido(self):
    lista = []
    self.__controlador_sistema.controlador_reservas.lista_reservas()
    self.__controlador_sistema.controlador_itens_cardapio.lista_itens_cardapio_formatado()

    dados_pedido = self.__tela_pedido.pega_dados_pedido()
    if dados_pedido == None:
      return
    codigo = dados_pedido["codigo"]
    id_reserva = dados_pedido["id_reserva"] 
    lista_itens = dados_pedido["lista_itens"]
    reserva = self.__controlador_sistema.controlador_reservas.pega_reserva_por_id(int(id_reserva))

    try: 
      if reserva is None:
        raise ReservaNaoExistenteException(dados_pedido["id_reserva"] )

      for pedido_existente in self.__pedido_DAO.get_all():
        if pedido_existente.codigo == codigo:
            raise PedidoRepetidoException(codigo)
        
      for num in lista_itens:
        item = self.__controlador_sistema.controlador_itens_cardapio.pega_item_por_cod(num)
        if item is None:
          raise ItemNaoExistenteException(num)
        lista.append(item)

      pedido = Pedido(codigo, reserva, lista)
      self.__pedido_DAO.add(pedido)
      self.__total_pedidos.add(pedido)

    except (PedidoRepetidoException, ReservaNaoExistenteException, ItemNaoExistenteException) as e:
        self.__tela_pedido.mostra_mensagem(str(e))
    

  def lista_pedidos(self):
    if len(self.__pedido_DAO.get_all()) == 0:
       self.__tela_pedido.mostra_mensagem("ATENÇÃO: Lista de pedidos vazia")
    dados_pedidos = []
    for pedido in self.__pedido_DAO.get_all():
        itens_pedido = ""
        for item in pedido.itens:
            if item is not None:
              itens_pedido += "{} - {} - {} - R$ {}\n".format(item.codigo_item, item.nome, item.descricao, item.preco)
            else:
              self.__tela_pedido.mostra_mensagem("Erro! Item é nulo!")

        dados_pedidos.append({"codigo": pedido.codigo, "id_reserva": pedido.reserva.id, "itens": itens_pedido})
    self.__tela_pedido.mostra_dados_pedido(dados_pedidos)


  def excluir_pedido(self):
    self.lista_pedidos()
    codigo = self.__tela_pedido.seleciona_pedido()
    if codigo == None:
      return
    pedido = self.pega_pedido_por_codigo(int(codigo))

    try:
      if (pedido is not None):
        self.__pedido_DAO.remove(pedido.codigo)
        self.lista_pedidos()
      else:
        raise PedidoNaoExistenteException(codigo)
    except PedidoNaoExistenteException as e:
      self.__tela_pedido.mostra_mensagem(e)
    
  def excluir_pedido_com_base_na_reserva(self, codigo):
    self.__pedido_DAO.remove(codigo)
    self.lista_pedidos()
    

  def pega_pedido_por_id_reserva(self, id_reserva: int):
     lista = []
     for pedido in self.__pedido_DAO.get_all():
      if(int(pedido.reserva.id) == int(id_reserva)):
        lista.append(pedido)
     return lista

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_pedido, 2: self.lista_pedidos, 3: self.excluir_pedido, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_pedido.tela_opcoes()]()

  @property
  def total_pedidos(self):
    return self.__total_pedidos.get_all()
  
  @property
  def pedidos(self):
    return self.__pedido_DAO.get_all()

  def apagar_pedidos(self):
    return self.__pedido_DAO.clear()
  
  def apagar_total_pedidos(self):
    return self.__total_pedidos.clear()