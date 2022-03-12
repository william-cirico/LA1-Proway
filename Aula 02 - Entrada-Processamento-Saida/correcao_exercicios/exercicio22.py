# Faça um programa que leia o nome de um vendedor, o seu salário fixo 
# e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que 
# este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o 
# total a receber no final do mês, com duas casas decimais.
nome: str = input("Digite o nome do vendedor: ")
salario_fixo: float = float(input("Digite o salário do vendedor: "))
total_vendas: float = float(input("Digite o total de vendas do vendedor: "))

salario_total: float = salario_fixo + total_vendas * .15

print(f"O salário total do funcionário é: {salario_total:.2f}")





