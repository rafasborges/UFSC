class MesaNaoExistenteException(Exception):
    def __init__(self, numero_mesa):
        self.mensagem = "A mesa de número {} não existe.".format(numero_mesa)
        super().__init__(self.mensagem)