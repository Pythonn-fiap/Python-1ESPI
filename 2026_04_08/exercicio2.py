#Exercício 02
#Implemente a função quadrado que recebe um número 
# e retorna o resultado desse número ao quadrado.

def numero_ao_quadrado(num) -> int:
    num = int(input("Digite um número inteiro: "))
    return num ** 2
print(f'Seu número ao quadrado é: {numero_ao_quadrado(5)}')