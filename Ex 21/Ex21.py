print('Vamos separar uma lista de numero inteiro com numero duplicados para uma lista sem duplicações')
def remover_duplicados(lista):
    lista_sem_duplicados = []
    for item in lista:
        if item not in lista_sem_duplicados:
            lista_sem_duplicados.append(item)
    return lista_sem_duplicados
entrada = input("Digite uma lista de inteiros separados por espaço: ")
lista = list(map(int, entrada.split()))
resultado = remover_duplicados(lista)
print("Lista sem duplicados:", resultado)