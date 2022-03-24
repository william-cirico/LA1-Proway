salario = float(input("Digite o salário: "))

salario_liquido = 0

if salario <= 0:
    salario_liquido = "Salário inválido"
elif salario <= 600:
    salario_liquido = "Isento"
elif salario <= 1200:
    salario_liquido = salario * .8
elif salario <= 2000:
    salario_liquido = salario * .75
else:
    salario_liquido = salario * .7

print(f"Salário líquido: {salario_liquido}")