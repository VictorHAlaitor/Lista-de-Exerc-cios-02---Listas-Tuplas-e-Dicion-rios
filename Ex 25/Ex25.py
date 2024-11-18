def filtrar_pares(lista):
    
    return [num for num in lista if num % 2 == 0]

entrada = input("Digite uma lista de inteiros separados por espaço: ")
lista = list(map(int, entrada.split()))

lista_pares = filtrar_pares(lista)
print("Números pares:", lista_pares)