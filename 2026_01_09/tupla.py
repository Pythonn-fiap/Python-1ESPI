#tupla
#ela é imutável, ou seja, não pode ser alterada depois de criada

print("Tupla")
minhaTupla = ('sol', 'agua', 'natureza')
print(minhaTupla)

print('\n Tupla com tipos de dados diferentes')
outraTupla = tuple(('a', 45, True))
print(type(outraTupla))
print(outraTupla)

print('\nAcessando pela posicao')
print(f'1a posicao: {minhaTupla[0]}')
print(f'2a posicao: {minhaTupla[1]}')

print('\nPegadinha')
tuplavazia = ()

print('\nPegadinha 2')
tuplaFalsa = ('Sol')
print(tuplaFalsa) #Para a tupla sair corretamente, é necessário colocar uma vírgula no final da tupla, assim: tuplaFalsa = ('Sol',)

print('\nAchando a posicao de um elemento')
minhaTupla = ('sol', 'agua', 'natureza')
print(minhaTupla)
print(f'A água esta na posicao: {minhaTupla.index("agua")}')




