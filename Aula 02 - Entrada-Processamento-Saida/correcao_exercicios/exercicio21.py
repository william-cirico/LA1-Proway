"""
O tempo que um ônibus leva para chegar a um destino qualquer é 15 min. Receba a hora e o minuto de 
saída do ônibus e mostre na tela qual será o horário de chegada ao destino.
"""
hora = int(input("Digite uma hora: "))
minuto = int(input("Digite uma minuto: "))

minuto_saida = minuto + 15
hora_saida = hora

if (minuto_saida >= 60):
    minuto_saida -= 60
    hora_saida += 1

if (hora_saida > 23):
    hora_saida = 0

print(f"{hora_saida:02}:{minuto_saida:02}")

