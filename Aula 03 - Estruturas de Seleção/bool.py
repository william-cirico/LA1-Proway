booleano: bool = False

print(bool(1))
print(bool(0))
print(bool(123971983719283712))
print(bool(-123971983719283712))
print(bool(1312.21))
print(bool(0.21))
print(bool(0.00))
print(bool("a"))
print(bool("0"))
print(bool(""))

valor = ""

if not valor:
    print("A variável está vazia")