""" As condições servem para selecionar quando uma parte do programa dever ativada ou simplesmente ignorada.

Exemplo:

As condicionais são 

if<condição>:
    <comando>

"""

# Exercício 1
""" Escreva um programa que pergunte a velocidade de um veiculo de um usuário.
    Caso ultaprasse 80 km, exiba um mensagem dizendo que o usuário foi multado, cobrando R$ 5 por Km acima de 80 km"""

velocidade = float(input("Qual a velocidade do seu carro? "))
if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f"Você foi multado por R${multa:.2f} por excesso de 80Km")
else:
    print("""Tenha um bom dia! Prossiga a viagem com segurança""")

# Exercicio 2
# Calculo do imposto de renda

salario = float(input("Qual o seu salário? R$"))
base = salario
imposto = 0

if base > 3000:
    imposto += (base - 3000) * 0.35
    base = 3000
if base > 1000:
    imposto += (base - 1000) * 0.20

print(f"Salario: {salario} Imposto a pagar: {imposto}")


# Exercicio 3
"""Escreva um programa que leia três numeros e que imprima o maior e o menor """
n1 = int(input("Insira um valor:"))
n2 = int(input("Insira um valor:"))
n3 = int(input("Insira um valor:"))

maior = 0
menor = 0

if n1 > n2 and n1 > n3:
    maior = n1
    menor = n2
if n2 > n3 and n2 > n1:
    maior = n2
    menor = n3
if n3 > n1 and n3 > n2:
    maior = n3
    menor = n1
print(f"Maior: {maior} Menor: {menor}")


# Exercicio 4
""" Escreva um programa que pergunte o salário para o funcionário e calcule o valor do aumento.
    Para salários superiores a 1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento e de 15%"""
salario = float(input("Qual o seu salário? "))

if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

novo_salario = salario + aumento

print(f"Seu novo salário é {novo_salario}")


# ELSE
""" Quando há problemas com o if, o else pode ser usado para simplificar o programa
já que caso a primeira condição seja uma e a segundo seja o inverso da primeira condição usamos
o else """

# Exemplo - Carro Velho

idade = int(input("Qual a idade de seu carro? "))

if idade <= 3:
    print("Seu carro é novo")
else:
    print("Seu carro é velho")

# Exercício 5
""" Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
E calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de ate 200km e R$ 0,45 para viagens mais longas"""

distancia = float(input("Qual a distancia que deseja percorrer? "))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f"Preço da passagem: {preco}")

# ESTRUTURAS ANINHADAS
""" Nem sempre os programas seram tão simples. Muitas vezes será necessario aninhar vários if
para obter o comportamento desejado o programa. Aninhar nesse caso é utilizar um if dentro de outro if"""

# Exemplo - Conta de telefone com três faixas de preço
minutos = int(input("Quanto minutos vc utilizou esse mês.:"))
if minutos < 200:
    preco = 0.20
else:
    if minutos < 400:
        preco = 0.18
    else:
        preco = 0.15
print(f"Preço da conta: R${minutos * preco}")

# Exemplo - Categori x preco

categoria = int(input("Qual a categoria do produto"))
if categoria == 1:
    preco = 10
elif categoria == 2:
    preco = 18
elif categoria == 3:
    preco = 23
elif categoria == 4:
    preco = 26
elif categoria == 5:
    preco = 31
else:
    print("Categoria inválida")
    preco = 0

print(f"Preço do produto: {preco:6.2f}")


# Exercicio 6
""" Escreva um programa que leia dois numeros e que pegunte qual a operação que será realizada
 Sendo soma, subtração, multiplicação, divisão e resto. Ao final, mostre o resultado da operação escolhida """
""" n1 = int(input("Insira um valor:"))
n2 = int(input("Insira um valor:"))

operacao = input(
    """ """Qual operação deseja realizar?
        (+) Soma
        (-) Subtração
        (*) Multiplicação
        (/) Divisão
        (%) Resto
""" """
)
if operacao == "+":
    print(f"O resultado da soma é {n1+n2}")
else:
    if operacao == "-":
        print(f"O resultado da subtração é  {n1-n2}")
    else:
        if operacao == "*":
            print(f"O resultado da multiplicacão é {n1*n2}")
        else:
            if operacao == "/":
                print(f"O resultado da divisão é {n1/n2}")
            else:
                if operacao == "%":
                    print(f"O resultado do resto é {n1%n2}") """

n1 = int(input("Insira um valor: "))
n2 = int(input("Insira um valor: "))

operacao = input(
    """Qual operação deseja realizar?
    (+) Soma
    (-) Subtração
    (*) Multiplicação
    (/) Divisão
    (%) Resto
   """
)

if operacao == "+":
    resultado = n1 + n2
elif operacao == "-":
    resultado = n1 - n2
elif operacao == "*":
    resultado = n1 * n2
elif operacao == "/":
    resultado = n1 / n2
elif operacao == "%":
    resultado = n1 % n2
else:
    print("Operação inválida!")

print("Resultado:", resultado)

# Exercíco 7
""" Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa deve ler o valor a comprar
o salario e quantidade de anos a pagar. O valor da prestação mensal não pode ser surperior a 30% do salario. Calcule o valor da prestaçaõ
como sendo o valor da casa a comprar divido pelo numero de meses a pagar."""

valor_casa = float(input("Qual o valor da casa? "))
salario = float(input("Qual o seu salário? "))
anos = int(input("Em quantos anos deseja pagar? "))

prestacao_mensal = valor_casa / (anos * 12)

if prestacao_mensal <= (salario * 0.3):
    print("Empréstimo aprovado!")
else:
    print("Empréstimo não aprovado!")
    sdada
