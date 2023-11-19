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
