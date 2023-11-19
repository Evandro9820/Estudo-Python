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
