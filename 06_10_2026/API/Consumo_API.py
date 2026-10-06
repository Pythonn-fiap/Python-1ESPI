#Consumo API

#API serve para recuperarmos dados a partir da chamada de um programa.
#Tipicamente esses programas estao disponiveis em alguma URL.

# aplicacao --> requisicao --> API --> resposta
#requisicoes sao feitas atraves de metodos HTTP (GET, POST, PUT, DELETE)

import requests

try:
    cep = input("Digite o CEP com 8 Dígitos: ")
    resposta = requests.get(f"http://viacep.com.br/ws/{cep}/json/")

    if resposta.status_code == 200:
        print("Requisição bem sucedida!")
        print(resposta.status_code)
        print(resposta.json())
    else:
        raise Exception(f"Erro na requisição: {resposta.status_code}")

except Exception as e:
    print(e)

