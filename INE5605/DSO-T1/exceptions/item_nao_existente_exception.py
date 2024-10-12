class ItemNaoExistenteException(Exception):
    def __init__(self, num):
        self.mensagem = "O item de número {} não existe.".format(num)
        super().__init__(self.mensagem)