class ItemCardapioRepetidoException(Exception):
    def __init__(self, codigo):
        self.mensagem = "O item com o código {} já existe"
        super().__init__(self.mensagem.format(codigo))