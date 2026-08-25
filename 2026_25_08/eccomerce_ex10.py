NOME, PRECO, ESTOQUE = 0, 1, 2


def listar_nomes_produtos(catalogo):
    return [produto[NOME] for produto in catalogo]


def listar_produtos_baixo_estoque(catalogo, limite=10):
    produtos_baixo_estoque = filter(
        lambda produto: produto[ESTOQUE] < limite, catalogo
    )
    return [produto[NOME] for produto in produtos_baixo_estoque]


def aplicar_reajuste_precos(catalogo, percentual):
    return [
        [
            produto[NOME],
            produto[PRECO] * (1 + percentual / 100),
            produto[ESTOQUE],
        ]
        for produto in catalogo
    ]


def calcular_valor_total_estoque(catalogo):
    total = 0
    for produto in catalogo:
        total = total + produto[PRECO] * produto[ESTOQUE]
    return total


if __name__ == "__main__":
    produtos = [
        ["Caderno", 12.50, 5],
        ["Caneta", 2.30, 100],
        ["Mochila", 89.90, 3],
        ["Estojo", 15.00, 8],
    ]

    nomes_baixo_estoque = [
        produto[NOME]
        for produto in produtos
        if produto[ESTOQUE] < 10
    ]

    print(nomes_baixo_estoque)
    print(listar_nomes_produtos(produtos))
    print(listar_produtos_baixo_estoque(produtos))

    catalogo_reajustado = aplicar_reajuste_precos(produtos, 10)
    print(catalogo_reajustado)
    print(calcular_valor_total_estoque(produtos))
