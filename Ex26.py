print('Mesclagem de dicionario')
def mesclar_dicionarios(dict1, dict2):
    dicionario_mesclado = dict1.copy()

    for chave, valor in dict2.items():
        if chave in dicionario_mesclado:
            dicionario_mesclado[chave] += valor
        else:
            dicionario_mesclado[chave] = valor

    return dicionario_mesclado

dict1 = {'a': 60, 'b': 20, 'c': 10}
dict2 = {'b': 15, 'c': 55, 'd': 5}

resultado = mesclar_dicionarios(dict1, dict2)

print("Dicionário mesclado:", resultado)    