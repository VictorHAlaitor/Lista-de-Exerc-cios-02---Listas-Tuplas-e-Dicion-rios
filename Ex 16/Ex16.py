print('Vamos calcular o fatorial de um numero')
def fatorial(n):
    if n <=1:
        return 1
    else:
            return n * fatorial (n - 1)
numero = int(input('Digite o numero que deseja calcular o fatorial: '))

if numero < 0:
    print('Não é possivel calcular o fatorial desse numero')
else:
    resultado = fatorial(numero)
    print(f'O fatorial de {numero} é {resultado}')