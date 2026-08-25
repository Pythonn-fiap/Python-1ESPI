#use list comprohension para criar uma lista com os quadrados de 1 a 10

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrados = [n **2 for n in numeros]
print(quadrados)


#list comprohesion para criar uma lista filtrando apenas numeros pares

numeros = [3,8,15,22,7,40,11]
pares = [n for n in numeros if n % 2 == 0]
print(pares)  # Saída: [8, 22, 40]

#Dada a lista numeros = [15, 42, 8, 99, 23] , use reduce com uma função lambda para
#encontrar o maior valor da lista, sem usar a função pronta max() .

 numeros = [15, 42, 8, 99, 23]



