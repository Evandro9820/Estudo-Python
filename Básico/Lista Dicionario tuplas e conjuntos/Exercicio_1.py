# Exercico 1
""" Calculo de média com notas digitadas """

notas = [0, 0, 0, 0, 0]
soma = 0
x = 0

while x < 5:
    notas[x] = float(input("Insira uma nota: "))
    soma += notas[x]
    x += 1
x = 0
while x < 5:
    print(f"Nota {x+1}: {notas[x]:5.2f}")
    x += 1
print(f"A media das notas é: {soma / 5:5.2f}")
