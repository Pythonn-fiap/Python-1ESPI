#Exercício 2 Dada a tupla numeros = (12, 45, 7, 23, 9, 31) , calcule a soma de todos os elementos
#percorrendo a tupla com um for (sem usar a função sum ) e imprima o total.

tuplaNumeros = (12, 45, 7, 23, 9, 31) #total = 127
soma = 0
for num in tuplaNumeros:
    soma += num
print(f'Total: {soma}')
