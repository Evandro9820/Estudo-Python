# Exercício 1
""" Escreva um programa que pergunte a velocidade de um veiculo de um usuário.
    Caso ultaprasse 80 km, exiba um mensagem dizendo que o usuário foi multado, cobrando R$ 5 por Km acima de 80 km"""

velocidade = float(input("Qual a velocidade do seu carro? "))
if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f"Você foi multado por R${multa:.2f} por excesso de 80Km")
else:
    print("""Tenha um bom dia! Prossiga a viagem com segurança""")
