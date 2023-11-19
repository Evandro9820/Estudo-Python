# Exercicio 6
""" Escreva um programa que leia dois numeros e que pegunte qual a operação que será realizada
 Sendo soma, subtração, multiplicação, divisão e resto. Ao final, mostre o resultado da operação escolhida """

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
