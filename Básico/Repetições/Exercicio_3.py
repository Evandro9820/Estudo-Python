# Exercicio 3
""" Faça um programa que receba do usuario um numero e exiba todos os numeros impares de 1 ate esse numero """
numero = int(input("Digite um numero: "))

for x in range(1, numero + 1):
    if x % 2 != 0:
        print(x)
