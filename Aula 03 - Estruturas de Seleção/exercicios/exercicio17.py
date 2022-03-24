idade = int(input("Digite a sua idade: "))

if idade < 16 or idade > 67:
    print("Não precisa votar")
elif idade >= 16 and idade < 18:
    print("Voto opcional")
else:
    print("Voto obrigatório")