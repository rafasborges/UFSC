class ReservaRepetidaException(Exception):
    def __init__(self, id):
        self.mensagem = "A reserva com id {} já existe"
        super().__init__(self.mensagem.format(id))