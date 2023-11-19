## Listas
Listas são um tipo de váriavel que permite o armazenamento de vários valores, acessados por um índice. Uma lista pode conter zero ou mais elementos de um mesmo tipo ou diversos, podendo conter inclusive outras listas. O tamanho de uma lista é igual a quantidade e elementos que ela possui
Assim podemos criar uma lista em python:

    L=[]

Como elas são muito flexiveis podemos criar uma lista com vários elementos só inserindo na lista

    L = [10,1,2]

Uma lista com três elementos, e também podemos dizer que que o primeiro elemento tem o indice 0 e o ultimo elemento tem o indice 2
    L[0]
    L[2]

### Trabalhando Com Indices
Vejemos outro exemplo: Um programa que lê cinco numeros, armazena-os em uma lista e depois solicita ao usuário que escolha um numero para mostar. O objetivo é por exemplo ler 15,12,5,7,9 e armazená-los na lista. Depois se o usuário digitar 2 ele imprimirá o segundo número digitado,3, o tericeiro, e assim suceessivamente. Observe que o indice do primeiro elemento é 0 e não 1: essa pequena conversão será feita no programa:

    numero = [0,0,0,0]
    x = 0 
    while x < 5:
        numeros[x] = int(input(f"Numero {x + 1 }"))
        x+=1

        while true:
            escolhido = int(input("Que posição você gostaria de imprimir (0 para sair).:"
            if escolhido == 0:
                break
            print(f"Você escolheu o Numero: {numeros[escolhido - 1]}")