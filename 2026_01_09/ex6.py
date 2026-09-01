#Exercício 6 Escreva uma função calcular_maior_menor que receba uma tupla de números e retorne
#uma tupla (maior, menor) com o maior e o menor valor encontrados

def calcular_maior_menor(tupla_numeros):
    maior = max(tupla_numeros)
    menor = min(tupla_numeros)
    return (maior, menor)
print(f'Maior e menor valor da tupla: {calcular_maior_menor((12, 45, 7, 23, 9, 31))}')

