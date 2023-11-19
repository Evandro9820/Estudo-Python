# Exercicio 2
""" Modifique o programa anterior para ler 7 ao inves de 5 notas """

notas = [0, 0, 0, 0, 0, 0, 0]
soma = 0
x = 0

while x < 7:
    notas[x] = float(input("Insira uma nota: "))
    soma += notas[x]
    x += 1
x = 0
while x < 7:
    print(f"Nota {x+1}: {notas[x]:5.2f}")
    x += 1
print(f"A media das notas é: {soma / 7:5.2f}")
