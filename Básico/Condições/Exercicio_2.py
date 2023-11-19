# Exercicio 2
# Calculo do imposto de renda

salario = float(input("Qual o seu salário? R$"))
base = salario
imposto = 0

if base > 3000:
    imposto += (base - 3000) * 0.35
    base = 3000
if base > 1000:
    imposto += (base - 1000) * 0.20

print(f"Salario: {salario} Imposto a pagar: {imposto}")
