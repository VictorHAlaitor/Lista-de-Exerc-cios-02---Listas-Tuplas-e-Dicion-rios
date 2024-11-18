print('Vamos dar uma lista dos numeros primos entre dois intervalos de numeros')
n1 = int(input('Informe o primeiro numero para o intervalo: '))
n2 = int(input('Informe o segundo numero para o intervalo: '))

def primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def primos_intervalo(n1, n2):
    primos = []
    for num in range(n1, n2 + 1):
        if primo(num):
            primos.append(num)
    return primos
lista_primo = primos_intervalo(n1,n2)
print(f'Os numeros primos são {lista_primo}')