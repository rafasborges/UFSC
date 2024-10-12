class ClienteRepetidoException(Exception):
    def __init__(self, cpf):
        self.mensagem = "O cliente com cpf {} já existe"
        super().__init__(self.mensagem.format(cpf))