#Utilize a API abaixo para gerar uma listagem com os nomes de N usuários. Exiba a lista em
#ordem alfabética

import requests

try:
    n = int(input("Digite o número de usuários a serem listados: "))
    resposta = requests.get(f"https://randomuser.me/api/?results={n}")

    if resposta.status_code == 200:
        dados = resposta.json()
        usuarios = [f"{usuario['name']['first']} {usuario['name']['last']}" for usuario in dados['results']]
        usuarios.sort()  # Ordena a lista em ordem alfabética
        print("Lista de usuários em ordem alfabética:")
        for usuario in usuarios:
            print(usuario)
    else:
        raise Exception(f"Erro na requisição: {resposta.status_code}")
except Exception as e:
    print(e)