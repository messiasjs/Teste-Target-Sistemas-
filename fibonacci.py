
#Questão 1 - Fibonacci
numero_informado = int(input("Digite um número: "))
ultimo=1
penultimo=0
termo = 0
sequencia=[]
pertence = False
while termo <= numero_informado:
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    sequencia.append(termo)

    if termo==numero_informado:
        pertence = True
        break
print("Alguns números da sequência: ", sequencia)
if pertence:
    
    print("O número ", numero_informado, "faz parte da sequência")

else :
    print("O número ", numero_informado, "não faz parte da sequência")
