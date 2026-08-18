#Dada a lista precos = [100.0, 250.0, 39.90] , use map com uma função lambda para gerar
#uma nova lista com 10% de desconto aplicado a cada preço.

precos = [100.0, 250.0, 39.90]
#Aplicando 10% de desconto usando map e lambda
descontos = list(map(lambda preco: preco * 0.9, precos))
print(descontos)  # Saída: [90.0, 225.0, 35.91]
