#Questão 2 - Faturamento 
import json

with open("dados.json", encoding='utf-8') as dados_json:
    dados = json.load(dados_json)

menor_indice = 0
maior_indice = 1
faturamento = []
menor_valor = dados[0]["valor"]
maior_valor = dados[0]["valor"]
contador =0
indices =[]
for dia in dados:
    valor = float(dia["valor"])
    faturamento.append(valor)
    
    #armazena o menor e maior valor faturado e o indice
    if valor < menor_valor and valor != 0.0 :
        menor_valor = valor
        menor_indice = faturamento.index(valor)
    elif valor > maior_valor:
        maior_valor = valor
        maior_indice = faturamento.index(valor)
    
    #armazenta quantidade de faturamento zerado
    if valor == 0.0:
        contador+=1

# calcula media de faturamento
media_faturamento = sum(faturamento)/(len(faturamento)-contador)
for dia in dados:
    valor = float(dia["valor"])
    #verifica se o valor é maior que a media
    if valor > media_faturamento:
        indices.append(faturamento.index(valor)+1)

print("O menor valor de faturamento ocorreu no dia ", menor_indice, " com o valor de ", menor_valor)
print("O maior valor de faturamento ocorreu no dia ", maior_indice, " com o valor de ", maior_valor)
print("A media de faturamento no mês foi de :", media_faturamento)
print("O faturamento alcançou a media nos dias: ", indices)
    