class CapacidadeDaMesaExcedidaException(Exception):
    def __init__(self, total_pessoas, capacidade):
        self.mensagem = " A capacidade da mesa é de {} pessoas, porém essa reserva conta com {} pessoas."
        super().__init__(self.mensagem.format(str(capacidade), str(total_pessoas)))