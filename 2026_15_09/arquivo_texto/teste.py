arquivo = open('arquivo.txt', 'r')

print(arquivo.read())
#se eu quiser voltar e ler o arquivo desde o inicio
#tenho que voltar o cursor para o inicio
print('\nVoltando para o inicio do arquivo')
arquivo.seek(0)
print(arquivo.readline(), end ='')
 
print('\nLendo como uma lista de linhas')
listaLinhas = arquivo.readlines()
print(listaLinhas)
 
#desafio: usando list comprehension tire o \n da lista
listaLimpa = [linha.replace("\n", "") for linha in listaLinhas]
print("\nLista sem \\n:", listaLimpa)

arquivo.close()


