print('Remoção de Elementos Duplicados de uma Lista Aninhada')
def remover_duplicados(lista_aninhada):
    return [list(set(sublista)) for sublista in lista_aninhada]

lista_aninhada = [
    [1, 2, 2, 3, 4, 4],
    [5, 6, 6, 7, 7],
    [8, 9, 9, 10, 10, 10]
]

resultado = remover_duplicados(lista_aninhada)

print("Lista com duplicados removidos:", resultado)