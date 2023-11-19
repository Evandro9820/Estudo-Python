# Exercício 5
""" Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
E calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de ate 200km e R$ 0,45 para viagens mais longas"""

distancia = float(input("Qual a distancia que deseja percorrer? "))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f"Preço da passagem: {preco}")
