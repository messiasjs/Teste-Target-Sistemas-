#Questão 4 - Inversão de caracteres
frase = input("Digite uma frase: ")
inverso = []
for i in range(len(frase)-1, -1,-1):
    inverso.append(frase[i])

invertida= ''.join(inverso)
print("String invertida: ",invertida)

