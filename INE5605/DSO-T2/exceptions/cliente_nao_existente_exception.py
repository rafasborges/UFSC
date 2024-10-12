class ClienteNaoExistenteException(Exception):
    def __init__(self, cpf_cliente):
        self.mensagem = "O cliente com CPF {} não existe.".format(cpf_cliente)
        super().__init__(self.mensagem)