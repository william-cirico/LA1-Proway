# LA1 Proway - Aula 03 - Exercícios
Os exercícios abaixo abordam questões relacionadas as estruturas de seleção:

-   Estruturas de seleção simples
-   Estruturas de seleção composta
-   Estruturas de seleção múltipla

Para a resolução dos exercícios abaixo crie um arquivo  **.py**  para cada uma das questões que forem relacionadas a lógica de programação. Ex.: exercicio01.py

1) Qual é a saída dos seguintes comandos:  
print(bool(not 10)) # ?  
print(bool("String")) # ?  
print(bool(2.3)) # ?  
print(bool(None)) # ?  

2) Qual é a saída das seguintes instruções:
print(10 > 2) # ?  
print(5 >= "5") # ?  
print("apple" > "pineapple") # ?  
print("2" > "12") # ?  
print(None > 10) # ?  
print(None == "\n0\n") # ?  

3) Escreva um script que **receba uma valor A**, verifique se o valor A é maior que 10 e
mostre na tela "O valor A é maior que 10".

	**Exemplo 01**
	**Entrada:** 
	11
	**Saída:**
	O valor A é maior que 10  
	Programa finalizado...
	
	**Exemplo 02**
	**Entrada:**
	9
	**Saída:**
	Programa finalizado...

4) Escreva um script que **receba um número**, se esse número for par mostre na tela
a metade do número digitado. No final do script mostrar na tela "Programa finalizado..."

	**Exemplo 01**  
	**Entrada:**  
	10  
	**Saída**:  
	5  
	Programa finalizado...  
	
	**Exemplo 02**  
	**Entrada:**  
	9  
	**Saída**:  
	Programa finalizado...  
	
5) Escreva um script que **receba um número**, se esse número for ímpar mostre na tela
o quadrado do número digitado. No final do script mostrar na tela "Programa finalizado..."

	**Exemplo 01**  
	**Entrada:**  
	10  
	**Saída**:  
	5  
	Programa finalizado...  
	
	**Exemplo 02**  
	**Entrada:**  
	9   
	**Saída**:  
	Programa finalizado...  

6) Escreva um script que receba um número, se esse número for par mostre na tela
"O número é par" senão mostre "O número é ímpar".

	**Exemplo 01**  
	**Entrada:**  
	10  
	**Saída:**
	O número é par  

	**Exemplo 02**  
	**Entrada:**  
	9  
	**Saída:**
	O número é par

7) Escreva um script que receba um número, se esse número estiver entre 20 e 90
mostre na tela "O número está na faixa entre 20 e 90" senão mostre "O número
está fora da faixa".

	**Exemplo 01**  
	**Entrada:**  
	21  
	**Saída:**  
	O número está na faixa entre 20 e 90  
	
	**Exemplo 02**  
	**Entrada:**  
		20  
	**Saída:**  
	 O número está fora da faixa  

	**Exemplo 03**  
	**Entrada:**  
	90  
	**Saída:**  
	O número está fora da faixa  

8) Considerando o valor de A = 10 e B = 20, responda a saída das seguintes expressões:  
print(A > 10 and B <= 20) # ?    
print(A > 10 or B <= 20) # ?  
print(A == 10 or B > 20) && B == 20) # ?  
print(None or 2 or "") # ?  
print(0 and 1) # ?  

9) Escreva um script que receba três valores A, B, C. Faça as comparações necessárias para exibir na tela o maior valor entre os três.

	**Exemplo 01**  
	**Entrada:**  
	10  
	12  
	2  
	**Saída:**  
	O maior número é 12 

	**Exemplo 02**  
	**Entrada:**  
	12  
	2  
	10  
	**Saída**:  
	O maior número é 12  

	**Exemplo 03**  
	**Entrada:**  
	2  
	10  
	12  
	**Saída:**  
	O maior número é 12

9) Reescreva o script abaixo utilizando o operador ternário:

	resultado = None  
	a, b = 10, 2  

	if a + b < 4:  
	&nbsp;&nbsp;&nbsp;&nbsp;resultado = "Abaixo"  
	else:  
	&nbsp;&nbsp;&nbsp;&nbsp;resultado = "Acima"  

	print(resultado)  


10) Escreva um programa que leia as medidas dos lados de um triângulo e
escreva se ele é Equilátero, Isósceles ou Escaleno. Sendo que:
* Triângulo Equilátero: possui os 3 lados iguais.
* Triângulo Isósceles: possui 2 lados iguais.
* Triângulo Escaleno: possui 3 lados diferentes.

11) Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz
quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que o
número é inválido.

12) Escreva um script para ler um número e informar se ele é divisível por 5.

13) Leia um número. Se o número for positivo imprima a raiz quadrada desse número. Do contrário, imprima o número ao quadrado.

14) Leia o salario de um trabalhador e o valor da prestação de um empréstimo. Se a prestaçao
for maior que 20% do salário imprima: “empréstimo não concedido”, caso contrario imprima:
“empréstimo concedido”.

15) Desenvolva um programa que recebe do usuário o placar de um jogo de futebol (os gols de cada time) e informe se o resultado foi um empate, a vitória do primeiro time ou do segundo time.

16) Desenvolva um programa que receba do usuário a sua idade e informe a situação de voto dele ("Não precisa votar", "Voto opcional", "Voto obrigatório").

17) Faça um script que leia três números e mostre-os em ordem decrescente.

18) Para doar sangue é necessário ter entre 18 e 67 anos. Faça um script que pergunte a idade de uma pessoa e diga se ela pode doar sangue ou não.  
Use o operador lógicos OU (or).

19) Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. Isto é, domingo se for 1, segunda-feira se for 2, e assim por diante.

20) Escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês correspondente a este número. Isto é, Janeiro se for 1, Fevereiro se 2, e assim por diante.

21) Faça um script que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N-Noturno.  
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

22) Escreva um algoritmo que peça o salário de uma pessoa e imprima o salário líquido, segunda a tabela a seguir:
<table>
	<tr>
		<td>Menor ou igual a R$ 600.00</td>
		<td>Isento</td>
	</tr>
	<tr>
		<td>Maior que R$ 600.00 e menor ou igual a R$ 1200.00</td>
		<td>20%</td>
	</tr>
	<tr>
		<td>Maior que R$ 1200.00 e menor ou igual a R$ 2000.00</td>
		<td>25%</td>
	</tr>
	<tr>
		<td>Maior que R$ 2000.00</td>
		<td>30%</td>
	</tr>
</table>