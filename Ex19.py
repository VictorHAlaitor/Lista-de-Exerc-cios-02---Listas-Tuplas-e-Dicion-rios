print('Vamos contar todos os caracteres de uma frase em forma de dicionário')
def contador(frase):
    contador = {}
    for char in frase:
        if char in contador:
            contador[char] += 1
        else:
            contador[char] = 1
    return contador
frase = input('Digite a frase desejada: ')
contar = contador(frase) 
print(f'Aqui está a contagem dos caracteres em forma de dicionário: {contar}')
