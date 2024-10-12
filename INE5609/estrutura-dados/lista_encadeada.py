#complexidade O[N]
class Node:
    def __init__(self, data):
        self._data = data
        self._next = None
    
class lista_encadeada:
    def __init__(self):
        self.head = None
        self._size = 0
        
    def append(self, elem):
        if self.head: #se já tem algum elemento na lista
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else: #lista estava vazia então: pirmiero elemento add
            self.head = Node(elem)
        self._size = self._size + 1
    
    def __len__(self):
        return self._size
    
    def _getnode(self):
        pointer = self.head
        for i in range(index - 1):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError ("list index out of range")
        return pointer 

    def set(self, index, elem):
        pass
    
    def __getitem__(self, index): #("A lista esta vazia ou a lista tem 3 elementos e o usuário pediu o índice 5")
        #a = lista[6]
        pointer = self._getnode(index)
        if pointer:
            return pointer.data
        else:
            raise IndexError("A lista esta vazia")
    
    def __setitem__(self, index, elem):
        # lista[5] = 9
        pointer = self._getnode(index)
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of range")
        
    def index(self, elem): #retrona o indice do elemento na lista
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == elem:
                return i
            pointer = pointer.next
                i = i + 1
            else:
                raise ValueError("{} não está na lista". format(elem))
            
    def insert(self, index, elem):
         node = Node(elem)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getnode(index-1)
            node.next = pointer.next
            pointer.next = node
        self._size = self._size + 1
    
    def remove(self, elem):
        if self.head == None:
            raise ValueError("{} is not in list".format(elem))
        elif self.head.data == elem:
            self.head = self.head.next
            self._size = self._size - 1
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while(pointer):
                if pointer.data == elem:
                    ancestor.next = pointer.next
                    pointer.next = None
                    self._size = self._size - 1
                    return True
                ancestor = pointer
                pointer = pointer.next
        raise ValueError("{} is not in list".format(elem))

    def __repr__(self):
        r = ""
        pointer = self.head
        while(pointer):
            r = r + str(pointer.data) + "->"
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()
                
                    
                
            
            
lista = lista_encadeada()
print(lista.size)
lista.append(5)
print(lista.size)
