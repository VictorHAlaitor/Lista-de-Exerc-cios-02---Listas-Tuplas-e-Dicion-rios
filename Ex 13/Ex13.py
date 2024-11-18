print('Vamos calcular a média das notas dos alunos')
notas = input('Informe as notas dos alunos separando elas por espaco ')
notas = [float(notas) for notas in notas.split()]
media = sum(notas) / len(notas)
print(f'A media das notas dos alunos é de {media}')