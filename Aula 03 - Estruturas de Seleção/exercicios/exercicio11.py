lado_a = int(input("Digite a medida do lado A do triângulo"))
lado_b = int(input("Digite a medida do lado B do triângulo"))
lado_c = int(input("Digite a medida do lado C do triângulo"))

if lado_a == lado_b and lado_b == lado_c:
    print("Triângulo Equilátero")
elif lado_a != lado_b and lado_b != lado_c and lado_c != lado_a:
    print("Triângulo Escaleno")
else:
    print("Triângulo Isósceles")