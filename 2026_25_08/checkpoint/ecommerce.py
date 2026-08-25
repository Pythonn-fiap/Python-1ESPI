# ecommerce.py
# Projeto de fundo - E-commerce simples
# Atividade avaliativa (conteúdo até a Aula 03): login de usuário e menus
# diferenciados.
#
# Complete as funções marcadas com TODO. Não altere as funções já prontas
# (elas vêm da Aula 03 e continuam funcionando exatamente como antes).

from functools import reduce

# ============================================================
# CONSTANTES
# ============================================================

# Índices de cada campo dentro da lista que representa um produto.
NOME = 0
PRECO = 1
ESTOQUE = 2

# FOI FEITO: constantes de posição dos dados do usuário.
NOME_USUARIO = 0
EMAIL = 1
SENHA = 2


# ============================================================
# SISTEMA — produtos (prontas desde a Aula 03, não alterar)
# ============================================================


def cadastrar_produto(
    catalogo: list[list[object]],
    nome: str,
    preco: float,
    estoque: int = 0,
) -> list[list[object]]:
    """Cadastra um novo produto no catálogo.

    Args:
        catalogo: matriz (lista de listas) com os produtos do e-commerce.
            Cada produto é representado como [nome, preco, estoque].
        nome: nome do produto a ser cadastrado.
        preco: preço unitário do produto.
        estoque: quantidade disponível em estoque. Padrão: 0 (produto
            cadastrado sem estoque inicial).

    Returns:
        O catálogo atualizado, incluindo o novo produto.
    """
    produto: list[object] = [nome, preco, estoque]
    catalogo.append(produto)
    return catalogo


def atualizar_estoque(
    catalogo: list[list[object]],
    nome_produto: str,
    quantidade: int,
) -> list[list[object]]:
    """Atualiza a quantidade em estoque de um produto já cadastrado.

    Args:
        catalogo: matriz (lista de listas) com os produtos do e-commerce.
            Cada produto é representado como [nome, preco, estoque].
        nome_produto: nome do produto cujo estoque será atualizado.
        quantidade: quantidade a ser somada ao estoque atual (pode ser
            negativa, para representar uma saída de estoque).

    Returns:
        O catálogo atualizado. Se o produto não for encontrado, o
        catálogo é retornado sem alterações.
    """
    for produto in catalogo:
        if produto[NOME] == nome_produto:
            produto[ESTOQUE] += quantidade
            return catalogo
    print(f"Produto '{nome_produto}' não encontrado no catálogo.")
    return catalogo


def exibir_catalogo(catalogo: list[list[object]]) -> None:
    """Exibe todos os produtos cadastrados no catálogo.

    Args:
        catalogo: matriz (lista de listas) com os produtos do e-commerce.
            Cada produto é representado como [nome, preco, estoque].

    Returns:
        None. Apenas imprime os produtos no console.
    """
    for produto in catalogo:
        print(
            f"{produto[NOME]} - R$ {produto[PRECO]:.2f} "
            f"(estoque: {produto[ESTOQUE]})"
        )


def listar_nomes_produtos(catalogo: list[list[object]]) -> list[str]:
    """Lista os nomes de todos os produtos cadastrados no catálogo.

    Args:
        catalogo: matriz (lista de listas) com os produtos do e-commerce.
            Cada produto é representado como [nome, preco, estoque].

    Returns:
        Uma lista com os nomes dos produtos, na mesma ordem do catálogo.
    """
    return [produto[NOME] for produto in catalogo]


def aplicar_reajuste_precos(
    catalogo: list[list[object]],
    percentual: float,
) -> list[list[object]]:
    """Aplica um reajuste percentual ao preço de todos os produtos.

    Gera um novo catálogo (nova matriz) com os preços reajustados,
    sem alterar o catálogo original.

    Args:
        catalogo: matriz (lista de listas) com os produtos do e-commerce.
            Cada produto é representado como [nome, preco, estoque].
        percentual: percentual de reajuste a ser aplicado. Valores
            positivos aumentam o preço, valores negativos representam
            desconto (ex.: -10 aplica 10% de desconto).

    Returns:
        Um novo catálogo, com os preços reajustados e o nome/estoque
        de cada produto preservados.
    """
    fator = 1 + (percentual / 100)
    return [
        [produto[NOME], round(produto[PRECO] * fator, 2), produto[ESTOQUE]]
        for produto in catalogo
    ]


def calcular_valor_total_estoque(catalogo: list[list[object]]) -> float:
    """Calcula o valor total investido em estoque.

    Soma, para cada produto, o valor de preco * estoque, usando reduce.

    Args:
        catalogo: matriz (lista de listas) com os produtos do e-commerce.
            Cada produto é representado como [nome, preco, estoque].

    Returns:
        O valor total investido em estoque (soma de preco * estoque de
        todos os produtos). Devolve 0.0 se o catálogo estiver vazio.
    """
    return reduce(
        lambda total, produto: total + produto[PRECO] * produto[ESTOQUE],
        catalogo,
        0.0,
    )


# ============================================================
# SISTEMA — produtos
# FOI FEITO: função para listar produtos com baixo estoque.
# ============================================================


def listar_produtos_baixo_estoque(
    catalogo: list[list[object]],
    limite: int = 10,
) -> list[str]:
    """Lista os nomes dos produtos com estoque abaixo de um limite.

    Args:
        catalogo: matriz (lista de listas) com os produtos do e-commerce.
            Cada produto é representado como [nome, preco, estoque].
        limite: quantidade mínima de estoque considerada "segura".
            Produtos com estoque menor que esse valor entram no
            resultado. Padrão: 10.

    Returns:
        Uma lista com os nomes dos produtos cujo estoque está abaixo do
        limite informado.
    """
    # Implementação com list comprehension e condição.
    return [
        produto[NOME]
        for produto in catalogo
        if produto[ESTOQUE] < limite
    ]


# ============================================================
# SISTEMA — usuários
# FOI FEITO: cadastro, verificação de e-mail e login de usuários.
# ============================================================


def cadastrar_usuario(
    usuarios: list[list[str]],
    nome: str,
    email: str,
    senha: str,
) -> list[list[str]]:
    """Cadastra um novo usuário, se o e-mail ainda não estiver em uso.

    Args:
        usuarios: matriz (lista de listas) com os usuários cadastrados.
            Cada usuário é representado como [nome, email, senha].
        nome: nome do usuário.
        email: e-mail do usuário (deve ser único).
        senha: senha do usuário.

    Returns:
        A lista de usuários atualizada. Se o e-mail já existir, a lista
        é retornada sem alterações.
    """
    if email_existe(usuarios, email):
        print("E-mail já cadastrado.")
        return usuarios

    usuario = [nome, email, senha]
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso.")
    return usuarios


def email_existe(usuarios: list[list[str]], email: str) -> bool:
    """Verifica se já existe um usuário cadastrado com o e-mail informado.

    Args:
        usuarios: matriz (lista de listas) com os usuários cadastrados.
            Cada usuário é representado como [nome, email, senha].
        email: e-mail a ser verificado.

    Returns:
        True se o e-mail já estiver cadastrado, False caso contrário.
    """
    for usuario in usuarios:
        if usuario[EMAIL] == email:
            return True
    return False


def fazer_login(
    usuarios: list[list[str]],
    email: str,
    senha: str,
) -> list[str] | None:
    """Verifica as credenciais e retorna o usuário correspondente.

    Args:
        usuarios: matriz (lista de listas) com os usuários cadastrados.
            Cada usuário é representado como [nome, email, senha].
        email: e-mail informado no login.
        senha: senha informada no login.

    Returns:
        A lista do usuário [nome, email, senha] se as credenciais
        conferirem, ou None caso contrário.
    """
    for usuario in usuarios:
        if usuario[EMAIL] == email and usuario[SENHA] == senha:
            return usuario
    return None


# ============================================================
# MENUS
# FOI FEITO: menus para usuários logados e não logados.
# ============================================================


def menu_cadastrar_usuario(usuarios: list[list[str]]) -> list[list[str]]:
    """Pede nome, e-mail e senha ao usuário e chama cadastrar_usuario.

    Args:
        usuarios: matriz (lista de listas) com os usuários cadastrados.

    Returns:
        A lista de usuários atualizada.
    """
    nome = input("Nome: ")
    email = input("E-mail: ")
    senha = input("Senha: ")
    return cadastrar_usuario(usuarios, nome, email, senha)


def menu_login(usuarios: list[list[str]]) -> list[str] | None:
    """Pede e-mail e senha, chama fazer_login e informa o resultado.

    Args:
        usuarios: matriz (lista de listas) com os usuários cadastrados.

    Returns:
        O usuário logado (lista [nome, email, senha]) se o login deu
        certo, ou None caso contrário.
    """
    email = input("E-mail: ")
    senha = input("Senha: ")
    usuario = fazer_login(usuarios, email, senha)

    if usuario is None:
        print("E-mail ou senha inválidos.")
    else:
        print(f"Login realizado. Olá, {usuario[NOME_USUARIO]}!")

    return usuario


def menu_produtos(catalogo: list[list[object]]) -> None:
    """Exibe o catálogo de produtos.

    Args:
        catalogo: matriz (lista de listas) com os produtos do e-commerce.

    Returns:
        None.
    """
    exibir_catalogo(catalogo)


def menu_logout() -> None:
    """Informa que o logout foi realizado com sucesso.

    Returns:
        None.
    """
    print("Logout realizado com sucesso.")


def menu_usuario_nao_logado(
    usuarios: list[list[str]],
    catalogo: list[list[object]],
) -> str | list[str] | None:
    """Menu mostrado a quem ainda não fez login.

    Opções: cadastrar usuário, fazer login, ver produtos, sair.

    Args:
        usuarios: matriz (lista de listas) com os usuários cadastrados.
        catalogo: matriz (lista de listas) com os produtos do e-commerce.

    Returns:
        "SAIR" se o usuário escolheu sair, o usuário logado (lista) se o
        login deu certo, ou None caso contrário.
    """
    print("\n ---- Bem-vindo ao meu e-commerce! ---- ")
    print("\n1 - Cadastrar usuário")
    print("2 - Fazer login")
    print("3 - Ver produtos")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        menu_cadastrar_usuario(usuarios)
    elif opcao == "2":
        return menu_login(usuarios)
    elif opcao == "3":
        menu_produtos(catalogo)
    elif opcao == "0":
        return "SAIR"
    else:
        print("Opção inválida.")

    return None


def menu_usuario_logado(
    usuario_logado: list[str],
    catalogo: list[list[object]],
) -> str | list[str] | None:
    """Menu mostrado a quem já está logado.

    Opções: ver produtos, logout, sair.

    Args:
        usuario_logado: usuário atualmente logado ([nome, email, senha]).
        catalogo: matriz (lista de listas) com os produtos do e-commerce.

    Returns:
        "SAIR" se o usuário escolheu sair, None se fez logout, ou o
        próprio usuario_logado caso continue logado.
    """
    print(f"\nOlá, {usuario_logado[NOME_USUARIO]}!")
    print("1 - Ver produtos")
    print("2 - Logout")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        menu_produtos(catalogo)
        return usuario_logado
    if opcao == "2":
        menu_logout()
        return None
    if opcao == "3":
        return "SAIR"

    print("Opção inválida.")
    return usuario_logado


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

if __name__ == "__main__":
    # Catálogo inicial de produtos (você pode reaproveitar os dados da
    # Aula 03 ou cadastrar os seus).
    catalogo: list[list[object]] = []
    catalogo = cadastrar_produto(catalogo, "Camiseta Azul", 59.90, 120)
    catalogo = cadastrar_produto(catalogo, "Tênis Runner", 199.90, 60)
    catalogo = cadastrar_produto(catalogo, "Boné Preto", 39.90, 50)

    usuarios: list[list[str]] = []
    usuario_logado: list[str] | None = None

    # FOI FEITO: loop principal para controlar login, logout e saída.
    while True:
        if usuario_logado is None:
            resultado = menu_usuario_nao_logado(usuarios, catalogo)
        else:
            resultado = menu_usuario_logado(usuario_logado, catalogo)

        if resultado == "SAIR":
            print("Programa encerrado.")
            break

        usuario_logado = resultado

