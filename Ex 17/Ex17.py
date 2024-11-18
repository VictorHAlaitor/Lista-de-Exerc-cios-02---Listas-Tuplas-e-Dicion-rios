
numeros = [3, -1, 4, -2, 5, -3, 2,6,-5,5,8,-21,50,-4,-7,-60,22,4,-45,56,-91]
print(f'Vamos ordenar essa lista {numeros} dos numeros negativos aos positivos')
ordenados = sorted(numeros, key=lambda x: x >= 0)
print(f'Os numero ordenados ficam assim {ordenados}')