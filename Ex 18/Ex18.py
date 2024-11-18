print('Vamos realizar uma soma de diagonais de uma matriz quadrada')
def diagonal(matriz):
    n = len(matriz)  
    soma1 = 0
    soma2 = 0
    for i in range(n):
        soma1 += matriz[i][i]  
        soma2 += matriz[i][n-i-1]  
    if n % 2 == 1:
        meio = n // 2
        soma2 -= matriz[meio][meio]
    return soma1, soma2

matriz = [
    [1, 2, 3, 5, 8],
    [4, 5, 6, 8, 4],
    [7, 8, 9, 4, 5]
]
soma1, soma2 = diagonal(matriz)
print(f"O resultado da soma da Diagonal Principal: {soma1}")
print(f"O resultado da soma da Diagonal Secundária: {soma2}")