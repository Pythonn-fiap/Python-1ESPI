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

# //////////////////////////////////////////////////////////////////////////////////////

#ex2 complementado

estoque = {}

while True:
    categoria = input("Categoria (ou 'fim'): ")
    if categoria == "fim":
        break

    estoque[categoria] = {}  

    while True:
        item = input(f"  Item em '{categoria}' (ou 'fim'): ")
        if item == "fim":
            break
        preco = float(input(f"  Preço de {item}: "))
        estoque[categoria][item] = preco

# Exemplo do resultado:
# {
#   "pendrive": {"pendrive": 50.0},
#   "papelaria": {"material": 3.0, "caderno": 39.0}
# }

# Para exibir:
for cat, itens in estoque.items():
    print(f"\n{cat}:")
    for item, preco in itens.items():
        print(f"  {item}: R$ {preco:.2f}")   

