# Exercicio 5
"""Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança
Exiba os valores mês a mês para os primeiros 24 meses. Escreva o Total de Juros Ganho no  Periodo"""

deposito_inicial = float(input("Insira o valor do deposito.: "))
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
