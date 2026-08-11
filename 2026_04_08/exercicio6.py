#Exercício 06
#Implemente a função soma_divisores, que recebe como parâmetro de entrada um número positivo
#e retorna a soma de todos os divisores desse número.
#Por exemplo:
# caso o número seja 15, o retorno deve ser 24 (1 + 3 + 5 + 15).
# caso o número seja 30, o retorno deve ser 72 (1 + 2 + 3 + 5 + 6 + 10 + 15 + 30)

def soma_divisores(num: int) -> int:
    soma = 0
    for i in range(1, num + 1):
        if num % i == 0:
            soma += i
    return soma

soma_divisores_num = int(input("Digite um número positivo: "))
print(f'A soma dos divisores de {soma_divisores_num} é: {soma_divisores(soma_divisores_num)}')