from abc import ABC, abstractmethod

class Tela(ABC):

    @abstractmethod
    def tela_opcoes(self):
        pass
    
    def le_num_inteiro(self, mensagem=" ", ints_validos=None):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_int = int(valor_lido) 
                if ints_validos and valor_int not in ints_validos:
                    raise ValueError  
                return valor_int
            except ValueError: 
                print("Valor incorreto!")
                if ints_validos:
                    print("Valores válidos: ", ints_validos)

    def mostra_mensagem(self, msg):
        print(msg)

    def checa_valor(self, texto):
        return any(char.isdigit() for char in texto)