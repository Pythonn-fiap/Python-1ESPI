#Exercício 3 Escreva uma função contar_pares que receba uma tupla de números inteiros e retorne
#quantos desses números são pares.

def contar_pares(tupla_numeros):
    contador = 0
    tupla_numeros = (12, 45, 7, 23, 9, 28)
    for num in tupla_numeros:
        if num % 2 == 0:
            print(f'{num} é par')
            contador += 1
    return contador

print(f'os numeros pares da tupla são: {contar_pares((12, 45, 7, 23, 9, 28))}')
