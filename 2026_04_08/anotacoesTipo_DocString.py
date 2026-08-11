#python possui tipagens dinamicas, por exemplo:
x = 10
print(type(x))  # <class 'int'>

nome = "paulo"
print(type(nome))  # <class 'str'>

#type hints ajuda a definir o tipo de dados esperados nas variaveis.
#porem ele apenas ajuda, ou seja o python nao impede que seja atribuido
#um valor de outro tipo de dados.

nome: str = "paulo"
print(type(nome))

nome = 123
print(type(nome))

#como visto acima, a linha vermelha indica que o tipo de dado nao 
# corresponde ao tipo definido na variavel, porem o python 
# nao impede que seja atribuido um valor de outro tipo de dado.

preco: float
preco = 7.8
print(type(preco))

#todos os tipos de dados sao aceitos no type hints
#int, float, bool, str, list, etc...
disponivel: bool = True
print(type(disponivel))

#o tipo de uso mais importante é quando definimos funções, ex:

def calcular_total(preco: float, quantidade: int) -> float:
    return preco * quantidade

print(calcular_total(preco, quantidade=2))
print(calcular_total(preco, quantidade=3))

# e quando a função nao tem retorno?
def exibir_produto(produto: str, preco: float) -> None:
    print(f"Produto: {produto}, Preço: {preco}")

exibir_produto("Leite", 8.9)

#mas o tipo list?
def somar_precos(precos: list[float]) -> float:
    return sum(precos)

