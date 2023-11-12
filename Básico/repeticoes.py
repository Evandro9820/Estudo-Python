""" As repetições representam a base de vários programas. Sendo utilizadas para executar a mesma parte de um programa várias vezes. Normamente dependendo de uma condição.
    
    Uma das estruturas de repitição é o while que repete um bloco enquanto a condição for verdadeira.
    Exemplo:
    while <condição>:
        <comando>
"""
# Execicio 1
""" Faça um programa para escrever a contagem regressiva de um lançamento de foquete. O programa deve imprimir 10,9,8,...,1,0 e FOGO! Na tela """

""" x = 10
while x >= 0:
    print(x)
    x -= 1
print("Lançar!") """

""" Outra estrutura de repetição usada são os contadores. """
# Exemplo
""" fim = int(input("Digite o ultimo numero que deseja imprimir.:"))

x = 1
while x <= fim:
    print(x)
    x += 1 """

""" Também podemos utilizar as condições dentro de uma estrutura de repetição. """
# Exemplo
""" x = 1
while x <= 10:
    if x % 2 == 0:
        print(f"{x} é par")
    else:
        print(f"{x} é ímpar")
    x += 1
 """

# Exercicio 2
""" Escreva um programa que mostre os 10 primeiro múltiplos de 3 """
""" multiplos = 0
numero = 3

while multiplos < 10:
    print(numero)
    numero += 3
    multiplos += 1
 """

# Exercicio 3
""" Faça um programa que receba do usuario um numero e exiba todos os numeros impares de 1 ate esse numero """
""" numero = int(input("Digite um numero: "))

for x in range(1, numero + 1):
    if x % 2!= 0:
        print(x)
 """

# Exercicio 4
""" Escreva um programa nque leia dos numeros. Imprima o resultado da multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e subtração para calcular o resultado.
    Lembre-se que podemos entender a multiplicação de dois numeros como somas sucessivas de um deles. Assim 4 x 5 = 4 + 4 + 4 + 4 + 4 """

""" numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite um numero: "))
resultado = 0 

while numero2 >0:
    resultado += numero1
    numero2 -= 1
print(f'O resultado da multiplicação é.: {resultado}')
 """

""" Outro recurso que podemos usar são os Acumuladores. Por exemplo em programas para calulcar o total de uma soma precisaremos de acumuladores. A diferença entre um contador e um acumulador é que o nos contadores o valor
 adicionado é constante e nos acumuladores, variavel. """
# Exemplo

n = 1
soma = 0
while n <= 10:
    x = int(input(f"Digite o {n} numero: "))
    soma += x
    n += 1
print(f"Soma.: {soma}")
