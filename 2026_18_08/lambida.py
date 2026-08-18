# Lambda
#Funcao anonima (pequena - de uma linha so - funcao inline  )
#A lambda e uma funcao anonima, ou seja, uma funcao sem nome. 
# Ela e usada para criar funcoes pequenas e simples, 
# que podem ser passadas como argumentos para outras funcoes.

def dobro(n: int) -> int:
    '''
    Calcula o dobro de um número.

    :param n: O número inteiro
    :return: O dobro do número fornecido
    '''
    return n * 2

#uso
print(dobro(5))  # Saída: 10

#transformando a funcao em lambda
ldobro = lambda n: n * 2
print(ldobro(5))  # Saída: 10

#uso mais comum
print((lambda n: n * 2)(5)) 

#lambda condicional
#tem um if embutido.

def maior(x:int, y:int) -> int:
    if x > y:
        return x
    else:
        return y
#uso
print(maior(10, 5))  # Saída: 10

#transformando a funcao em lambda
lmaior = lambda x, y: x if x > y else y
print(lmaior(4,5))  # Saída: 5

#uso mais comum
print((lambda x, y: x if x > y else y)(10, 20))  # Saída: 20

#posso o usar o print dentro do lambda
#pode mas nao e recomendado, pois o lambda deve ser usado para funcoes pequenas e simples.
lmenor = lambda x, y: print(x) if x < y else print(y)
xpto = lmenor (10,20)
print(lmenor(10, 20))

#a melhor solucao
lmenor2 = lambda x, y: (
    f'entre {x} e {y}, o menor e {x if x < y else y}'
)
print(lmenor2(8,23))  # Saída: entre 10 e 20, o menor e 10


#Map ~e uma funcionalidade do python que permite aplicar 
#uma funcao em todos os elementos de uma colecao (lista, tupla, dicionario, etc)

def dobro (n:int) -> int:
    return n * 2
numeros = [1, 2, 3, 4, 5]

#com o map
print(list(map(dobro, numeros)))
