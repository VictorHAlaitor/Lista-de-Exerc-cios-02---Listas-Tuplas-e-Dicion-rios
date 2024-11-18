print('Vamos verificar os anagramas')
def verificar_anagrama(palavra1, palavra2):
   
    palavra1 = palavra1.replace(" ", "").lower()
    palavra2 = palavra2.replace(" ", "").lower()
        
    return sorted(palavra1) == sorted(palavra2)

palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

if verificar_anagrama(palavra1, palavra2):
    print("As palavras são anagramas.")
else:
    print("As palavras não são anagramas.")
