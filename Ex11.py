print('Olá, iremos separar uma frase em palavras unicas')
frase = input('Por gentileza escreva a frase que deseja saber o numero de palavras unicas usadas: ')
palavra = frase.lower().split()
unicas = set(palavra)
palavras_unicas = len(unicas)
print(f'A frase informada possui {palavras_unicas} palavras unicas')