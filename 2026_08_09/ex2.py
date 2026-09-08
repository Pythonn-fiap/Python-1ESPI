# Preencha um dicionário com as informações de 5 produtos. Utilize o nome do produto como chave e o
#preço como valor. Solicite os dados ao usuário. Percorra o dicionário e exiba o nome dos produtos com
#preço superior a R$ 50,00.

info = {}

for i in range(5):
    nome_produto = input(f"Informe o nome do {i+1}º produto: ")
    preco_produto = float(input(f"Informe o preço do {i+1}º produto: "))
    info[nome_produto] = preco_produto

# Mostrar os produtos com preço superior a R$ 50,00
print("\nProdutos com preço superior a R$ 50,00:")
for nome, preco in info.items():
    if preco > 50:
        print(f"Produto: {nome} -> Preço: R$ {preco:.2f}")