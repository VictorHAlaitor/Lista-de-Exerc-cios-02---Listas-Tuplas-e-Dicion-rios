print('Vamos aprender da tabuada do 1 ao 10 de um numero')
tabuada = int(input('Informe o numero que deseja aprender a tabuada: '))

for count in range(10):
    print('%d x %d = %d' % (tabuada, count+1, tabuada*(count+1)))
    