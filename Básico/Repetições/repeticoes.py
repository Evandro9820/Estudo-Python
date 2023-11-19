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

""" n = 1
soma = 0
while n <= 10:
    x = int(input(f"Digite o {n} numero: "))
    soma += x # Acumulador
    n += 1 # é Um contador
print(f"Soma.: {soma}") """

# Ao Invés de usarmos cinco variaveis, vamos acumular os valores à medida que são lidos.

""" x = 1
soma = 0
while x <= 5:
    n = int(input(f"{x} Digite um número.:"))
    soma += n
    x += 1
print(f"A média é {soma / 5:5.2f}")
 """
""" Exercicio 1 
Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança
Exiba os valores mês a mês para os primeiros 24 meses. Escreva o Total de Juros Ganho no  Periodo"""

""" deposito_inicial = float(input("Insira o valor do deposito.: "))
taxa_juros = float(input("Insira o valor dos Juros Mensais.: "))
x = 0
saldo = deposito_inicial
total_juros = 0

while x < 24:
    juros = deposito_inicial + taxa_juros / 100
    saldo += juros
    total_juros += juros
    x += 1
    print(f"Saldo no Mẽs {x} .: {saldo:10.2f}")
print(f"Total de Juros Ganho foi de {total_juros:2f}")
 """

""" Exercicio 2
Altere o programa anterior de forma que ele também peça o deposito mensal, e esse valor será depositado no inicio de cada
mês, e você deve considera=lo para o calculo de juros do Mês seguinte"""


""" deposito_inicial = float(input("Insira o valor do deposito.: "))
taxa_juros = float(input("Insira o valor dos Juros Mensais.: "))
deposito_mensal = float(input("Insira o valor do deposito mensal: "))
x = 0
saldo = deposito_inicial
total_juros = 0

while x < 24:
    juros = deposito_inicial + taxa_juros / 100
    saldo += juros + deposito_mensal
    total_juros += juros
    x += 1
    print(f"Saldo no Mẽs {x} .: {saldo:10.2f}")
print(f"Total de Juros Ganho foi de {total_juros:0.2f}") """

""" Exercicio 3 
Escreva um Programa que pergunte o valor inicial de uma divida e o juro mensal.
Pergunte também o valor mensal que será pago. Imprima o  número de meses para que a dívida seja paga, o total de juros e o valor total da divida."""

""" valor_original = float(input("Insira o valor inical da dívida.: "))
juros_mensais = float(input("Insira o valor dos Juros Mensais.: "))
valor_mensal = float(input("Insira o valor do valor mensal.: "))
x = 0
total_juros = 0
total_divida = 0
divida = valor_original

while divida > 0:
    juros = valor_original * (juros_mensais / 100)
    total_juros += juros
    divida += juros_mensais - valor_mensal
    x += 1

print(f"Número de meses para pagar a dívida: {x}")
print(f"Total de juros pagos: {total_juros:0.2f}")
print(f"Valor total da dívida: {valor_original + total_juros}") """

""" Interrompendo a Repetição
Embora seja util, a estrutura while só verifica sua condição de para no inicio de cada repitição
Dependendo do problema, a habilidade de terminar o while dentro do bloco a repetir pode ser interessante 
A instrução break é utilizada par interromper a execução do while independente do valor atual de sua condição 
Exemplo.:"""

""" s = 0
while True:
    v = int(input("Digite um valor ou 0 para sair : "))
    if v == 0:
        break
    s += v

    print(s)
 """

""" Exercicio 1
Escreva um programa para controlar uma pequena maquina registradora. Você deve solicitar ao usuario que digite o código do produto e a quantidade comprada
"""

tabuada = 1
while tabuada <= 10:
    numero = 1
    while numero <= 10:
        print(f"{tabuada} X {numero} = {tabuada * numero}")
        numero += 1
    tabuada += 1
