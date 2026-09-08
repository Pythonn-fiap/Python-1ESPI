# Dicionario sao colecoes do tipo formulario
# chave: valor

# exemplo: nome = "Joao"
#          Idade = 20
#          Sexo = "Masculino"

# Nao sao posicionais, ou seja, nao tem indice
# permitem tipo de dados diferentes
# permitem valores repetidos, porem chaves sao unicas
# permitem inclusão, alteracao e exclusao, portanto sao mutaveis.

print("Dicionario\n")
aluno = {"nome": 'Joao', "idade": 20, "sexo": "Masculino"}
print(aluno)
print(type(aluno))

print("\nAcessando valores do dicionario:")
print(aluno["nome"])
print(aluno["idade"])
print(aluno["sexo"])

print("\nDicionario vazio")
vazio = {}
print(vazio)

print("\nAdicionando valores ao dicionario vazio:")
vazio['categoria'] = 'brinquedos'
print(vazio)

aluno['profissao'] = 'estagiario'
print(aluno)

print('\nAlterando valores')
aluno['nome'] = 'Bruno'
print(aluno)
print(aluno.get('nome'))
aluno.update({'idade' : 18})
print(aluno)

print('\nRemovendo valores')
aluno.pop('idade') # elimina segundo uma chave
print(aluno)
del aluno['sexo'] # elimina uma chave, del é uma exclusao generica
print(aluno)
aluno.popitem()
print(aluno)

print('\nLimpa o dicionario')
aluno.clear()
print(aluno)

###ATENCAO###
#Consigo sempre alterar valores
#Mas nunca chaves
aluno = {'nome': 'Gustavo', 'sexo': 'masculino', 'profissao': 'estagiario'}
print(aluno)
aluno['profissao'] = 'analista junior'
print(aluno)
#aqui ele nao troca, ele acaba acrescentando um valor no dicionario
aluno['profissao carteira'] = 'analista junior'
print(aluno)
#como trocar a chave, precisa eliminar e recriar
del aluno['profissao carteira']
aluno.pop('profissao')
aluno['profissao carteira'] = 'analista junior'
print(aluno)
 
print('\nPercorrendo ou varrendo o dicionario')
aluno = {'nome': 'Gustavo', 'idade': 18, 'sexo': 'masculino', 'profissao carteira': 'analista junior'}
for caracteristicas in aluno:
    print(caracteristicas)
print('\nSomente as chaves')
for chave in aluno.keys():
    print(chave)
print('\nSomento os valores')
for valor in aluno.values():
    print(valor)
print('\nSomente os valores pela chaves')
for chave in aluno:
    print(aluno[chave])
 
print('\nOs itens completos')
for item in aluno.items():
    print(item)
print('\nOs itens ja separados com atribuicao multiplos')
for chave, valor in aluno.items():
    print(f'{chave} = {valor}')

#atribuicao multipla

x, y, z = 10, 20, 30
print(f'x = {x}, y = {y}, z = {z}')

#na maior parte das colecoes a copia se da pela igualdade
#vamos examinar o dicionario, que é uma colecao mutavel
print("\n")
original = {'cafe', 'pao', 'leite'}
copiafalsa = original
copia = original.copy()
copia = original
print(f'original: {original}')
print(f'copiafalsa: {copiafalsa}')
print(f'copia: {copia}')
# conjuntos usam `add`, não `append`
copiafalsa.add('cachorro')
copia.add('cachorro')
print(f'original: {original}')
print(f'copia: {copia}')

print("\nCopiando o dicionario")
aluno = {'nome': 'Bruno', 'idade': 18, 'sexo': 'masculino', 'profissao carteira': 'analista junior'}
aluno['nome'] = 'Bruno Santos'
print(aluno)