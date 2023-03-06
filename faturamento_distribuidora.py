#Questão 3 - Faturamento distribuidora
faturamento_estado = [{"estado":"SP", "valor":"67836.43"},
{"estado":"RJ", "valor":"36678.66"},
{"estado":"MG", "valor":"29229.88"},
{"estado":"ES", "valor":"27165.48"},
{"estado":"Outros", "valor":"19849.53"}]

total_distribuidora = 0
for estado in faturamento_estado:
    valor = float(estado["valor"])    
    total_distribuidora+=valor

print("Faturamento total: ", total_distribuidora)
print("Percentual de representação por estado")
for estado in faturamento_estado:
    valor = float(estado["valor"])    
    porcentagem = (valor*100)/total_distribuidora
    print(estado["estado"], ": {:.2f}".format(porcentagem),"%")
