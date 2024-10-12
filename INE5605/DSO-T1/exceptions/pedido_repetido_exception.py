class PedidoRepetidoException(Exception):
    def __init__(self, codigo):
        self.mensagem = "O pedido com código {} já existe"
        super().__init__(self.mensagem.format(codigo))