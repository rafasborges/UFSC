class ReservaNaoExistenteException(Exception):
    def __init__(self, id):
        self.mensagem = "A reserva de id {} não existe.".format(id)
        super().__init__(self.mensagem)