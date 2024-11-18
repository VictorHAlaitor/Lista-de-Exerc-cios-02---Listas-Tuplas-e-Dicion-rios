print("Vamos verificar o Sudoku")
def verificar_sudoku(tabuleiro):
    def verifica_unicidade(lista):
        lista = [num for num in lista if num != 0]  
        return len(lista) == len(set(lista))  

    for linha in tabuleiro:
        if not verifica_unicidade(linha):
            return False

    for coluna in range(9):
        if not verifica_unicidade([tabuleiro[linha][coluna] for linha in range(9)]):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [tabuleiro[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if not verifica_unicidade(subgrid):
                return False

    return True

tabuleiro_sudoku = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

if verificar_sudoku(tabuleiro_sudoku):
    print("O tabuleiro de Sudoku é válido.")
else:
    print("O tabuleiro de Sudoku não é válido.")