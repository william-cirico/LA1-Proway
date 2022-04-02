N = int(input("Digite o valor de N: "))

for i in range(1, N + 1):
    if i % 2 == 0:
        print(f"{i} - Par")
    else:
        print(f"{i} - Ímpar")