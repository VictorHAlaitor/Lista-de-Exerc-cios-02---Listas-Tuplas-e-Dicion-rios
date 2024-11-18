print('Vamo verificar se uma palavra é um palindromo')
palavra = input('Informe a palavra que deseja verificar: ')
palavra = palavra.strip().lower()
if palavra == palavra[::-1]:
    print(f'A palavra "{palavra}" é um palindromo ')
else:
    print(f'A palavra "{palavra}" não é um palindromo')