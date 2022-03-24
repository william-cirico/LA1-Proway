salario = float(input("Digite o salário do funcionário: "))
valor_prestacao = float(input("Valor da prestação: "))

porcentagem_salario = salario * .2

if valor_prestacao > porcentagem_salario:
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido")