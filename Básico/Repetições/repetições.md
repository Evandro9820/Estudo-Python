# Repetições

As repetições representam a base de vários programas. Sendo utilizadas para executar a mesma parte de um programa várias vezes. Normamente dependendo de uma condição.
    
Uma das estruturas de repitição é o while que repete um bloco enquanto a condição for verdadeira.
Exemplo:
    
    while <condição>:
        <comando>

Um coisa usada em conjunto com uma estrutura de repetiçãoo são os contadores
    
    fim = int(input("Digite o ultimo numero que deseja imprimir.:"))

    x = 1
    while x <= fim:
    print(x)
    x += 1 """

Também podemos utilizar as condições dentro de uma estrutura de repetição.
     x = 1
    while x <= 10:
        if x % 2 == 0:
            print(f"{x} é par")
        else:
            print(f"{x} é ímpar")
    x += 1

Outro recurso que podemos usar são os Acumuladores. Por exemplo em programas para calulcar o total de uma soma precisaremos de acumuladores. A diferença entre um contador e um acumulador é que o nos contadores o valor adicionado é constante e nos acumuladores, variavel.
    
    n = 1
    soma = 0
    while n <= 10:
        x = int(input(f"Digite o {n} numero: "))
        soma += x # Acumulador
        n += 1 # é Um contador
    print(f"Soma.: {soma}")

Ao Invés de usarmos cinco variaveis, vamos acumular os valores à medida que são lidos.
    
    x = 1
    soma = 0
    while x <= 5:
        n = int(input(f"{x} Digite um número.:"))
        soma += n
        x += 1
    print(f"A média é {soma / 5:5.2f}")

Interrompendo a Repetição
Embora seja util, a estrutura while só verifica sua condição de para no inicio de cada repitição
Dependendo do problema, a habilidade de terminar o while dentro do bloco a repetir pode ser interessante 
A instrução break é utilizada par interromper a execução do while independente do valor atual de sua condição 
Exemplo.:    

    s = 0
    while True:
        v = int(input("Digite um valor ou 0 para sair : "))
        if v == 0:
            break
        s += v
    print(s)

## Repetições Aninhadas 

Podemos combinar vários while de forma a obter resultador mais interessantes  como a repetição com incremento de duas váriaveis. Imagine imprimir as tabuadas de multiplicação de 1  a 10. Exemplo:

    tabuada = 1
    while tabuada<=10:
        numero = 1 
        while numero<=10:
            print(f"{tabuada} X {numero} = {tabuada * numero}")
        numero+=1
    tabuada+=1    