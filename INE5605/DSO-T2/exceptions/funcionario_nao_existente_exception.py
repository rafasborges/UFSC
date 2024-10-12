class FuncionarioNaoExistenteException(Exception):
    def __init__(self, nome_funcionario):
        self.mensagem = "O funcionário '{}' não existe.".format(nome_funcionario)
        super().__init__(self.mensagem)