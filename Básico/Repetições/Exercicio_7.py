""" Exercicio 3 
Escreva um Programa que pergunte o valor inicial de uma divida e o juro mensal.
Pergunte também o valor mensal que será pago. Imprima o  número de meses para que a dívida seja paga, o total de juros e o valor total da divida."""

valor_original = float(input("Insira o valor inical da dívida.: "))
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
print(f"Valor total da dívida: {valor_original + total_juros}")
