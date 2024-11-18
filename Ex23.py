print('Vamos realizar calculos basicos, informe dois valores e qual operação matematica desejada')
def calculadora():
    
    num1 = float(input("Digite o primeiro valor: "))
    num2 = float(input("Digite o segundo valor: "))
    operacao = input("Escolha a operação (+, -, *, /): ")

    
    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            return "Não é possível dividir por zero!"
    else:
        return "Operação inválida!"

    return f"O resultado de {num1} {operacao} {num2} é: {resultado}"
print(calculadora())