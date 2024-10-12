import random 
def busca_binaria(lista, elem, comeco = 0, fim  = None):
    if end is None: #para nao ter que colocar na hora do teste: busca_binaria(lista, 4, 0, len(lista) -1)
        end = len(lista) -1 
    if comeco <= fim:
        meio = (comeco + fim) //2
        if lista[meio] == elem:
            return meio
        elif elem < lista[meio]:
            return busca_binaria(lista, elem, comeco, meio-1)
        else: #elem > lista[meio]
            return bsuca_binaria(lista, elem, meio+1, fim)
    return None

#teste para busca binária
empty = []
single = [7]
pair = [3, 7]
odd = [1, 2, 3, 5, 7, 8, 9, 13, 27, 31, 43]
even = [1, 2, 3, 5, 7, 8, 9, 13, 27, 31, 43, 70]
repeated = [1, 2, 2, 5, 5, 5, 9, 13, 21, 21, 21, 21]

def test_empty():
    if busca_binaria(empty, random.randint(0, 1000)) is not None:
        return False
    return True
    
def test_single():
    if busca_binaria(single, 7) :
        return False
    if busca_binaria(single, 10) is not None:
        return False
    return True

if __name__ == "__main__":
    print("*******************************")
    if test_empty():
        print("PASSOU VAZIO")
    else:
        print("FALHOU VAZIO")
    if (test_single()):
        print("PASSOU UNICO")
    else:
        print("FALHOU ÚNICO")

    test_cases = { 
                  'Dupla': pair, 
                  'Ímpar': odd,
                  'Par': even,
                  'Repetido': repeated
                }
    again = 's'
    while(again == 's'):
        for name, lista in test_cases.items():
            print("\nCaso de teste: {}\n{}".format(name, lista))
            # seleciona na lista
            e = int(input("Elemento a ser buscado: "))
            i = busca_binaria(lista, e)
            print("\n Índice encontrado:", i)
        again = input("Repetir? (S/N): ").lower()
    print("*******************************")
