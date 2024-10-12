class MesaRepetidaException(Exception):
    def __init__(self, numero):
        self.mensagem = "A mesa com número {} já existe"
        super().__init__(self.mensagem.format(numero))
        
