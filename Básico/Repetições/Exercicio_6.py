""" Exercicio 6
Altere o programa anterior de forma que ele também peça o deposito mensal, e esse valor será depositado no inicio de cada
mês, e você deve considera=lo para o calculo de juros do Mês seguinte"""

deposito_inicial = float(input("Insira o valor do deposito.: "))
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
print(f"Total de Juros Ganho foi de {total_juros:0.2f}")
