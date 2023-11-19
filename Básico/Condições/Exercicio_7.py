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
