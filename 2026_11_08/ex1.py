nome = 0
idade = 1
cidade = 2




def mostrar_info(info:list[list[object]], 
                      nome:str, idade:int, cidade:str) -> list[list[object]]:
    informacoes = [nome,idade,cidade]
    info.append(informacoes)
    return info

infor = [
    [
        input("DIGITE SEU NOME: "),
        int(input("DIGITE SUA IDADE: ")),
        input("DIGITE SUA CIDADE: ")
    ]
]

def exibir_info(info:list[list[object]]) -> None:
    for informacoes in info:
        print(f'Nome: {informacoes[nome]} | Idade: {informacoes[idade]} anos | Cidade: {informacoes[cidade]}')

exibir_info(infor)
