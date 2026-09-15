#Exercício 1 Leia um número inteiro digitado pelo usuário e imprima o seu quadrado (o número elevado
#ao quadrado). Trate ValueError caso o valor informado não seja um número inteiro.
while True:
    try:
        numero = int(input("Digite um numero"))
        quadrado = numero ** 2
        quadrado = numero
        if quadrado == numero:
            print(f"{numero} ao quadrado é {quadrado}")
            break

    except ValueError:
        print("Entrada Invalida, Digite um Número Inteiro... ")
    



