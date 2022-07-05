# Construa um script que leia o preço de um produto, o percentual 
# de desconto e calcule o valor a pagar e o valor do desconto
preco: float = float(input("Digite o preço do produto: "))
percentual_desconto: float = float(input("Digite o percentual de desconto do produto: "))

desconto: float = percentual_desconto / 100 * preco
valor_total: float = preco - desconto

print(f"Preço: {preco}")
print(f"% de desconto: {percentual_desconto}")
print(f"Valor total: {valor_total}")
print(f"Desconto: {desconto}")

