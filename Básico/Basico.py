""" Os operadores e operaçãoes matematica em python são:

    + - Adição
    - Subtração
    * Multiplicação
    // Divisão Inteira
    / Divisão com resultado fracionário
    % Modulo ou resto
    ** Exponenciação
    Exemplos:
    """

print(10 + 20 * 30)
print(4**2 / 30)
print((9**4 + 2) * 6 - 1)

# Imprima seu nome na tela
print("Evandro")

# Escreva um programa que exiba o resultado de 2a x 3b, em que a = 3 e b =5

a = 3
b = 5

resultado = (2 * a) * (3 * b)

print(resultado)

# Escreva um programa que calcule a soma de três variaveis e exiba o resultado

a = 10
b = 20
c = 30

resultado = a + b + c

print(resultado)

# Crie um programa que calcule o aumento de 15% para um salário de R$750

salario = 750
aumento = salario * 0.15

print(aumento)

print("-----------------------------------------------------\n")


# Crie um programa que determine se uma pessoa terá que pagar imposto ou não. Considerando que o salario é de R$1200,00

salario = 1300
imposto = salario * 0.08
if salario > 1200:
    print(f"O seu salário de R${salario:.2f} custará R${imposto:.2f} de imposto")
else:
    print("Nao e preciso declarar imposto")

print("-----------------------------------------------------\n")

# Crie um progrssama que irá decidir se um aluno foi aprovado ou reprovado. Considerando que a média é 7 tendo três matérias nessa conta

""" nota1 = float(input("Digite a nota da primeira matéria: "))
nota2 = float(input("Digite a nota da segunda matéria: "))
nota3 = float(input("Digite a nota da terceira matéria: ")) """
nota1 = 7
nota2 = 4
nota3 = 5

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado.")

# Variaveis de String
print("-----------------------------------------------------\n")
print("O aluno foi aprovado ou reprovado com a nota média de %f" % (media))
# A maneira acima já caiu em desuso pelos programas, o que está sendo mais comumente usando é o format para compor as strings sendo uma forma mais moderna de se fazer isso
print(f"A nota média do aluno é de {media}")
""" 
As entradas de dados são feitas atráves do comando input
Exemplo:
x  = input("Digite algo:")

A variavel x recebe a informação, e dai dá sequencia ao programa para trata-la da melhor maneira

Existe também a conversão de dados na entrada de dados, porque a função input sempre retorna valores strings então usandos o tipo antes do input 
Exemplo

anos = int(input("Anos de Serviço"))

Com isso convertemos para o tipo de desejado

Execícios
"""

print("-----------------------------------------------------\n")
# Faça um programa que peça dois numeros inteiros. Imprima a soma desses dois numeros na tela
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

print(n1 + n2)

# Escreva um programa que leia um valor em metros e o exiba convertido em milimetros
metros = float(input("Digite o valor em metros: "))
milimetros = metros * 1000
print(f"O valor em milímetros é: {milimetros}")

# Escreva um programa que calcule o aumento salarial de um funcionario. Ele deve solicitar o valor do salario e a porcentagem do aumento.E exiba o valor do aumento e do novo salario
salario = float(input("Digite o valor do salário: "))
porcentagem_aumento = float(input("Digite a porcentagem do aumento: "))

aumento = salario * (porcentagem_aumento / 100)
novo_salario = salario + aumento

print(f"O valor do aumento é: {aumento}")
print(f"O novo salário é: {novo_salario}")

# Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto e exiba o valor do desconto e o preço a pagar
preco = float(input("Digite o preço da mercadoria: "))
percentual_desconto = float(input("Digite o percentual de desconto: "))

valor_desconto = preco * (percentual_desconto / 100)
preco_pagar = preco - valor_desconto
print(f"O valor do desconto é: {valor_desconto}")
print(f"O preço a pagar é: {preco_pagar}")
