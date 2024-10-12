class NaoHaMesasDisponiveisException(Exception):
    def __init__(self):
        self.mensagem = "Não há mesas disponíveis no momento."
        super().__init__(self.mensagem)