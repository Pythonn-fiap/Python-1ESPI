#Exercício 7 Comece com a lista lista_nomes = ["Ana", "Bruno", "Carla"] . Converta essa lista em uma
#tupla tupla_nomes . Em seguida, como a tupla não pode ser alterada, converta-a de volta para lista,
#adicione o nome "Diego" e converta essa lista final novamente em tupla. Imprima o resultado de cada
#etapa.

lista_nomes = ["Ana", "Bruno", "Carla"]
tupla_nomes = tuple(lista_nomes)
print(f'Tupla: {tupla_nomes}')

lista_nomes = list(tupla_nomes)
lista_nomes.append("Diego")
tupla_nomes = tuple(lista_nomes)
print(f'Tupla final: {tupla_nomes}')