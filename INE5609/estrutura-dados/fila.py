class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self._size = 0 #tamanho da fila
    
    def inserir(self, elem):
        none = Node(elem) #elem que acabou de chegar dentro de um nó
        if self.ultimo is None: #casa a fila for vazia, o último recebe esse novo elem
            self.ultimo = node
        elif self.primeiro is None:
            self.primeiro = elem 
        else:
            self.last.next = node #o ultimo elem reconhece agora o novo ultimo elem da fila
            self.last = node #o ultimo elem recebe o novo numero
            
        self._size = self._size + 1 #add um novo espaço na memória
    
    def remover(self): #remover o primeiro FIFO 
        if self._size > 0:
            elem = self.primeiro.data
            self.priemiro = self.primeiro.next
            self._size = self._size - 1
            return elem
        else: #self._size < 0
            raise IndexError ("A fila está vazia!")
    
    def retornar(self): #retornar o primeiro 
        if self._size > 0:
            elem = self.primeiro.data
            return elem
        else: #self._size < 0
            raise IndexError ("A fila está vazia!")
        
    def __len__(self): #Retrona o tamanho da fila
        return self._size
    
    def __repr__(self):
        is self._size > 0:
            r = ""
            while (pointer):
                r = r + str(pointer.data) + " "
                pointer = pointer.next
            return r 
        else:
            raise IndexError ("A fila está vazia!")
        