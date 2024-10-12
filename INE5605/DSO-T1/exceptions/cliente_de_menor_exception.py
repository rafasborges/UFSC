class ClienteDeMenorException(Exception):
    def __init__(self, idade):
        self.mensagem = " Apenas responsáveis maiores permitidos! O cliente possui {} anos, portando não é de maior."
        super().__init__(self.mensagem.format(idade))