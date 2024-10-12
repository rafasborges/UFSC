class PedidoNaoExistenteException(Exception):
    def __init__(self, codigo):
        self.mensagem = "O pedido de código {} não existe.".format(codigo)
        super().__init__(self.mensagem)