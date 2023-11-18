# Exercicio 8
""" Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada
O programa deve exibir o total de compras depois do usuario digitar 0 qualquer outro código deve exibir a mensagem de erro 'Produto inexistente' """


produto = int(input("Insira o código do produto.:"))
compra = int(input("Insira a quantidade comprada.:"))

while True:
    if produto == 1:
        preco = 0.50
        valor_total = compra * preco
        print(
            f"Foi comprado {compra} Cachorro quente no valor de {preco} dando {valor_total} no total"
        )
        break
    elif produto == 2:
        preco = 1.00
        valor_total = compra * preco
        print(
            f"Foi comprado {compra} X-Salada no valor de {preco} dando {valor_total} no total"
        )
        break

    elif produto == 3:
        preco = 1.50
        valor_total = compra * preco
        print(
            f"Foi comprado {compra} X-Bacon no valor de {preco} dando {valor_total} no total"
        )
        break
    elif produto == 4:
        preco = 2.00
        valor_total = compra * preco
        print(
            f"Foi comprado {compra} Torrada simples no valor de {preco} dando {valor_total} no total"
        )
        break

    elif produto == 5:
        preco = 2.50
        valor_total = compra * preco
        print(
            f"Foi comprado {compra} Torrada com Cheese no valor de {preco} dando {valor_total} no total"
        )
        break

    elif produto == 6:
        preco = 3.00
        valor_total = compra * preco
        print(
            f"Foi comprado {compra} Refrigerante no valor de {preco} dando {valor_total} no total"
        )
        break
    elif produto == 0:
        break
    else:
        print("Produto inexistente")
        break
