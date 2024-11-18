print('Vamos realizar a sequencia de fibonacci de um')
def fibonacci(n):
    fibs = [0, 1]  
    while len(fibs) < n:
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[:n]
numero = int(input('Digitem um numero para gerar a sequencia: '))
print(f'Os numeros da sequencia são: {fibonacci(numero)}')