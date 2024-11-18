print('Vamos saber a media das suas 3 provas')
p1 = int(input('Informe sua primeira nota: '))
p2 = int(input('Informe sua segunda nota: '))
p3 = int(input('Informe sua terceira nota: '))
def som(p1,p2,p3):
    return (p1+p2+p3) / 3
soma = som(p1,p2,p3) 
print(f'A sua média é {soma}')