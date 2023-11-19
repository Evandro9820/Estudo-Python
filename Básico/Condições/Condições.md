# Condições

## IF
As condições server para selecionar quando uma parte do programa deverá ser executada, no python a estrutura de decisão é o if. Com o seguinte formato:

    if<condição>:
        <comando>

 Ele não é nada mais que o nosso "se", sendo possível entender ele como se a condição for verdadeira faça algo.

## ELSE
Também temos o else que usando para avaliar se a condição é falsa sem precisar de um novo if.
Exemplo:
    idade = int(input("Qual a idade de seu carro? "))

    if idade <= 3:
        print("Seu carro é novo")
    else:
        print("Seu carro é velho")

## Estruturas Aninhadas

Nem sempre tudo será simples. Muitas das vezes será nessario aninhar vários if para obter o comportamento desejado do programa. Aninhar no caso é utilizar um if dentro de outro if.

Exemplo:
    minutos = int(input("Quanto minutos vc utilizou esse mês.:"))
    if minutos < 200:
        preco = 0.20
    else:
        if minutos < 400:
        preco = 0.18
    else:
        preco = 0.15
    print(f"Preço da conta: R${minutos * preco}")

## Elif
elif é uma abreviação de "else if", que significa "senão se". É usado para testar várias condições em sequência, após uma condição if ter falhado.
        if condição1:
        # código a ser executado se a condição1 for verdadeira
    elif condição2:
        # código a ser executado se a condição2 for verdadeira
    elif condição3:
        # código a ser executado se a condição3 for verdadeira
    else:
        # código a ser executado se nenhuma das condições anteriores for verdadeira