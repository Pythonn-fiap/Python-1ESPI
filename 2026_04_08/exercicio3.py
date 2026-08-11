##Implemente a função soma_dos_quadrados que receba 
# dois numeros e devolve a soma dos seus quadrados.
#Você pode tentar reutilizar a função quadrado definida anteriormente para facilitar a implementação.


def quadrado(num: int) -> int:
    return num ** 2


def soma_dos_quadrados(num1: int, num2: int) -> int:
    return quadrado(num1) + quadrado(num2)


num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))
print(f'A soma dos quadrados é: {soma_dos_quadrados(num1, num2)}')
