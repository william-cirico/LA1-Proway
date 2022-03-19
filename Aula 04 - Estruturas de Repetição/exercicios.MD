# LA1 Proway - Aula 04 - Exercícios

Os exercícios abaixo abordam questões relacionadas as estruturas de repetição:

* Laço for
* Laço while
* break e continue

Para a resolução dos exercícios abaixo crie um arquivo .py para cada uma das questões que forem relacionadas a lógica de programação. Ex.: exercicio01.py

1) Faça dois scripts que mostrem a mensagem "Olá mundo!" 10 vezes na tela. Utilize uma estrutura
de repetição diferente em cada um dos scripts (for e while).


2) Elabore três scripts que mostrem a mensagem "Estou aparecendo pela <numero_de_vezes> na tela!" 10 vezes. Substitua <numero_de_vezes> pela iteração atual do loop. Utilize uma estrutura de repetição diferente em cada um dos scripts
(for e while).


3) Faça um algoritmo que mostra uma contagem regressiva na tela, iniciando em 10 e terminando em 0. Mostrar uma mensagem “FIM!” apos a contagem.


4) Faça um script utilizando o for, que permita ao usuário fazer três contas de subtração. 
Para isso peça ao usuário dois números a cada iteração do loop e mostre na tela o resultado
da operação.  
    **Entrada:**                
    1                         
    2                       
    4                                            
    3  
    9  
    5  

    **Saída:**  
    1 - 2 = -1  
    4 - 3 = 1  
    9 - 5 = 4  


5) Escreva um programa que declare uma váriavel numero, inicialize-a com 0, e incremente-a de 1000
em 1000, mostrando seu valor na tela, ate que seu valor seja 100000 (cem mil).


6) Faça um programa que peça ao usuario para digitar 5 valores. Ao final, mostre a soma desses
valores e média desses valores (arredondado para duas casas decimais).  
    **Entrada:**             
    9                        
    8                      
    2  
    3  
    4  

    **Saída:**   
    Soma: 26  
    Média: 5.20  


7) Faça um programa que receba um número N e mostre na tela todos os números ímpares de 0
até N.  
    **Entrada:** 
    5    
    **Saída:**
    1, 3, 5                  


8) Crie um algoritmo que peça ao usuário um número e mostre na tela a tabuada (1 à 10) desse número.  
    **Entrada:**                  
    2  
    **Saída:**  
    2 x 1 = 2  
    2 x 2 = 4  
    2 x 3 = 6  
    2 x 4 = 8  
    2 x 5 = 10  
    2 x 6 = 12  
    2 x 7 = 14  
    2 x 8 = 16  
    2 x 9 = 18  
    2 x 10 = 20                        
                        
9) Escreva um script que leia 5 valores do usuário e mostre quantos desses valores digitados são negativos.  
**Entrada:**                
1                       
-2  
3  
-5  
4  
**Saída:**  
2

10) Elabore um  algoritmo que receba 10 números diferentes e mostre quantos são pares e quantos são ímpares.  
**Entrada:**                 
1                        
9                        
2  
3  
13  
2  
92  
7  
11  
14  
**Saída:**  
Pares: 4  
Ímpares: 6  

11) Faça um script que receba valores inteiros e mostre na tela quantos desses valores recebidos estão no intervalo [10, 20] e quantos não estão. O programa irá parar de pedir números quando o usuário digitar um número negativo.  
**Entrada:**           
10                      
12                      
21  
32  
14  
-1  
**Saída:**  
3 números estão no intervalo  
2 números estão fora do intervalo  

12) Construa um programa que leia vários valores númericos enquanto um valor negativo não for digitado. Após isso,
mostre a média aritmética dos valores recebidos.  
**Entrada:**               
3                       
5  
10  
-1  
**Saída:**  
6


13) Elabore um script que mostre na tela os 15 primeiros múltiplos de 7.  
**Saída** 
7 14 21 28 35 42 49 56 63 70 77 84 91 98 105 


14) Escreva um algoritmo que receba um número e calcule o fatorial desse número.  
**Entrada:**             
5    
**Saída:**
120                 

15) A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e número
de filhos. A prefeitura deseja saber:  
a) média do salário da população  
b) média do número de filhos  
c) maior salário  

    Crie um script que leia as informações necessários do usuário enquanto o salário digitado não for negativo. 
    Após isso informe as informações solicitadas.  
    **Entrada:**              
    3000                      
    3                         
    2000                      
    1  
    4000  
    1  
    -100  
    **Saída:**  
    Média salarial: 3000  
    Média de filhos: 1.67  
    Maior salário: 4000  


16) Crie um script que leia 5 valores e mostre qual o maior e o menor valor lido.  
    **Entrada:**              
    -1                    
    0                     
    9  
    2  
    3  
    **Saída:**  
    O menor valor digitado foi -1  
    O maior valor digitado foi 9


17) Faça um programa que simule a urna eleitoral. Apresente um menu com as seguintes informações para o usuário:  
1 - José Bolinha  
2 - Maria Nascimento  
3 - João da Silva  
4 - Voto nulo  
5 - Voto em branco  
Após isso, leia o voto digitado pelo usuário até que ele digite o valor 0. Ao final mostre:
    - Total de votos para cada candidato;
    - Total de votos nulos;
    - Total de votos em branco.  

    **Entrada:**             
    1                      
    1                      
    2                      
    3                      
    3                      
    4                      
    5  
    0

    **Saída:**  
    Total de Votos  
    José Bolinha: 2 voto(s)  
    Maria Nascimento: 1 voto(s)  
    João da Silva: 2 voto(s)  
    Votos nulos: 1 voto(s)  
    Votos em branco: 1 voto(s)  


18) Faça um algoritmo que mostre os conceitos finais dos alunos de uma classe de 4 alunos.  
a) a média de cada aluno será fornecida pelo usuário.  
b) a tabela de conceitos se encontra abaixo:  
    <table>
        <tr>
            <th>Nota</th>
            <th>Conceito</th>
        </tr>
        <tr>
            <td>de 0.0 à 4.9</td>
            <td>D</td>
        </tr>
        <tr>
            <td>de 5.0 à 6.9</td>
            <td>C</td>
        </tr>
        <tr>
            <td>de 7.0 à 8.9</td>
            <td>B</td>
        </tr>
        <tr>
            <td>de 9.0 à 10.0</td>
            <td>A</td>
        </tr>
    </table>


19) Escreva um algoritmo que calcule a média aritmética das 3 notas dos alunos de uma classe. 
O algoritmo deverá ler, além das notas, o código do aluno e deverá ser encerrado quando o código for igual a zero.
    **Entrada:**           
    0012021                  
    10                      
    8  
    9  
    0022021  
    10  
    10  
    10  
    0  
    **Saída:**  
    A média do aluno com a matrícula 0012021 é 9.00  
    A média do aluno com a matrícula 0022021 é 10.00  


20) Faça um programa que receba dois numeros. Calcule e mostre:
    - a soma dos numeros pares desse intervalo de números, incluindo os números digitados;
    - a multiplicaçao dos números ímpares desse intervalo, incluindo os números digitados;  
    <br/>

    **Entrada:**          
    1                     
    10       
    **Saída:**  
    Soma dos pares: 30  
    Multiplicação dos ímpares: 945           


21) Faça um algoritmo que calcule e mostre os 20 primeiros números primos.  
**Saída:**  
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71

22) Faça um programa que receba um número n e mostra na tela os n primeiros números bem como a informação se o número é ímpar ou par.  
**Entrada**:  
5  
**Saída**:  
1 - Ímpar  
2 - Par  
3 - Ímpar  
4 - Par  
5 - Ímpar  