# 1a Cadastrar produto
# parametros: catalago, produto, nome do produto, valor, quantidade
# Exemplo depois e cadastrado
# [['Camiste azul', 89,90, 50], ['Cachecol', 35.00, 30]]

nome = 0
preco = 1
estoque = 2

def cadastrar_produto(catalogo:list[list[object]], 
                      nome:str, preco:float, estoque:int) -> list[list[object]]:
    produto = [nome, preco, estoque]
    catalogo.append(produto)
    return catalogo


#2 funcao

loja = [
    ['Camiseta Azul', 89.90, 10],
    ['tenis jeffrey', 666.6, 6]
]

def exibir_catalogo(catalogo: list[list[object]]) -> None:
    for produto in catalogo:
        print(f'{produto[nome]} - R$ {produto[preco]:.2f} ({produto[estoque]} em estoque)')


exibir_catalogo(loja)