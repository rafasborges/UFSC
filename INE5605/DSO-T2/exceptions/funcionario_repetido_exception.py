class FuncionarioRepetidoException(Exception):
    def __init__(self, cpf):
        self.mensagem = "O funcionário com esse cpf {} já existe"
        super().__init__(self.mensagem.format(cpf))