import random
print('Vamos jogar um jogo de adivinhação!!! Advinhe um numero de 1 a 100   ')

numero_secreto = random.randint(1, 100)
tentativas = 0 
nome = input('Informe o seu nick de Jogador: ')
print(f'Vamos começar {nome}')
while True:
    
    chute = int(input('digite o seu chute: '))
    tentativas += 1
    if chute < numero_secreto:
        print(f'Você errou {nome}, o numero correto é maior que {chute}!!')
    elif chute > numero_secreto:
        print(f'Você errou {nome}, o numero correto é menor que {chute}!!')
    else:
        print(f'PARABÉS {nome} !!!!! {chute} é o numero correto!!!!!!') 
        break