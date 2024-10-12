from exceptions.capacidade_da_mesa_excedida_exception import CapacidadeDaMesaExcedidaException
from exceptions.nao_ha_mesas_disponiveis_exception import NaoHaMesasDisponiveisException
from exceptions.reserva_nao_existente_exception import ReservaNaoExistenteException
from exceptions.reserva_repetida_exception import ReservaRepetidaException
from exceptions.mesa_nao_existente_exception import MesaNaoExistenteException
from exceptions.cliente_nao_existente_exception import ClienteNaoExistenteException
from exceptions.funcionario_nao_existente_exception import FuncionarioNaoExistenteException
from limites.tela_reserva import TelaReserva
from entidades.reserva import Reserva


class ControladorReserva():

  def __init__(self, controlador_sistema):
    self.__controlador_sistema = controlador_sistema
    self.__reservas = []
    self.__total_reservas = []
    self.__tela_reserva = TelaReserva()

  def pega_reserva_por_id(self, id: int):
    for reserva in self.__reservas:
      if(int(reserva.id) == int(id)):
        return reserva
    return None

  def incluir_reserva(self):
    self.__controlador_sistema.controlador_clientes.lista_clientes()
    self.__controlador_sistema.controlador_funcionarios.lista_funcionarios()
    self.__controlador_sistema.controlador_mesas.lista_mesas_disponiveis()

    dados_reserva = self.__tela_reserva.pega_dados_reserva()
    id = dados_reserva["id"]

    cliente = self.__controlador_sistema.controlador_clientes.pega_cliente_por_cpf(dados_reserva["cliente_cpf"])
    funcionario = self.__controlador_sistema.controlador_funcionarios.pega_funcionario_por_nome(dados_reserva["funcionario_nome"])
    mesa = self.__controlador_sistema.controlador_mesas.pega_mesa_por_numero(dados_reserva["mesa_num"])

    try:
        if mesa is None:
            raise MesaNaoExistenteException(dados_reserva["mesa_num"])
        if cliente is None:
            raise ClienteNaoExistenteException(dados_reserva["cliente_cpf"])
        if funcionario is None:
            raise FuncionarioNaoExistenteException(dados_reserva["funcionario_nome"])
        
        for reserva in self.__reservas:
            if reserva.id == id:
                raise ReservaRepetidaException(id)

        if not self.__controlador_sistema.controlador_mesas.ha_mesas_disponiveis():
            raise NaoHaMesasDisponiveisException()

        total_pessoas = int(cliente.num_convidados) + 1
      
        if int(mesa.capacidade) < total_pessoas:
            raise CapacidadeDaMesaExcedidaException(total_pessoas, mesa.capacidade)

        reserva = Reserva(id, cliente, funcionario, mesa)
        mesa.status = True
        self.__reservas.append(reserva)
        self.__total_reservas.append(reserva)
        
    except (MesaNaoExistenteException, ClienteNaoExistenteException, FuncionarioNaoExistenteException, ReservaRepetidaException, CapacidadeDaMesaExcedidaException, NaoHaMesasDisponiveisException) as e:
        self.__tela_reserva.mostra_mensagem(str(e))


  def lista_reservas(self):
    self.__tela_reserva.mostra_mensagem("------ RESERVAS ------")
    if len(self.__reservas) == 0:
       self.__tela_reserva.mostra_mensagem("ATENÇÃO: Lista de reservas vazia")
    for e in self.__reservas:
      self.__tela_reserva.mostra_reserva({"nome_cliente": e.cliente.nome,
                                                "nome_funcionario": e.funcionario.nome,
                                                "num_mesa": e.mesa.numero,
                                                "id_reserva": e.id,
                                                })

  def excluir_reserva(self):
    self.lista_reservas()
    id_reserva = self.__tela_reserva.seleciona_reserva()
    reserva = self.pega_reserva_por_id(int(id_reserva))
    
    try:
      if (reserva is not None):
        self.__reservas.remove(reserva)
        self.lista_reservas()
        reserva.mesa.status = False
      else:
        raise ReservaNaoExistenteException(id_reserva)
    except ReservaNaoExistenteException as e:
       self.__tela_reserva.mostra_mensagem(e)


  def calcular_ganho_reserva(self):
    self.lista_reservas()
    id_reserva = self.__tela_reserva.seleciona_reserva()
    total = 0
    pedidos = self.__controlador_sistema.controlador_pedidos.pega_pedido_por_id_reserva(int(id_reserva))
    for pedido in pedidos:
      for item in pedido.itens:
        total += int(item.preco)
    self.__tela_reserva.mostra_ganho_reserva(id_reserva, total)

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_reserva, 2: self.lista_reservas, 3: self.excluir_reserva, 4: self.calcular_ganho_reserva, 5: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_reserva.tela_opcoes()]()

  @property
  def total_reservas(self):
     return self.__total_reservas
  
  @property
  def reservas(self):
     return self.__reservas