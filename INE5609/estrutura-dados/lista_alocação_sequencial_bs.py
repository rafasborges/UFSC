def busca(lista, elem):
    "Retorna o índice do elem se ele estiver na lista, caso contrário retorna None"
    for i in range(len(lista)):
        if lista[i] == elem:
            return i
    return None
    
lista_diferente = [2, 5, 8, "oi", 10, "chocolate]"]
elemento = 10

indice = busca(lista_diferente, elemento)
if indice is not None:
    print("O índice do elemento {} é {}.".format(elemento, indice))
else:
    print("O elemento {} não está na lista.".format(elemento))
