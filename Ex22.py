print('Vamos seperar as vogais e a consoantes de uma frase')
def contar_vogais_consoantes(frase):
    vogais = "aeiouAEIOU"  
    consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"  

    contador_vogais = 0
    contador_consoantes = 0

    for char in frase:
        if char in vogais:
            contador_vogais += 1
        elif char in consoantes:
            contador_consoantes += 1

    return contador_vogais, contador_consoantes
frase = input("Digite a frase que deseja separar as vogais e consoantes: ")
vogais, consoantes = contar_vogais_consoantes(frase)
print(f"Aqui estão as Vogais da frase: {vogais}, e aqui as Consoantes da frase: {consoantes}")

