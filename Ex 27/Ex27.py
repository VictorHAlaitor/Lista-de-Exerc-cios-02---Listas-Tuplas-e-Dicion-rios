print('Contatdo de Palavras Frequentes')
from collections import Counter
import re

def contar_palavras_frequentes(texto):
    texto = re.sub(r'[^\w\s]', '', texto).lower()
    
    palavras = texto.split()
    
    contador = Counter(palavras)
    
    return contador.most_common(5)

texto = input("Digite um texto longo: ")

palavras_frequentes = contar_palavras_frequentes(texto)

print("As 5 palavras mais frequentes são:")
for palavra, frequencia in palavras_frequentes:
    print(f"{palavra}: {frequencia}")