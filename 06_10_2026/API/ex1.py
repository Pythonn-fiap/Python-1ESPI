#Solicite ao usuário a sigla de uma UF e utilize a API abaixo para consultar e exibir os nomes
#de todos os municípios da UF informada

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

try:
    uf = input("Digite a sigla da UF (ex: SP, RJ, MG): ").strip().upper()
    resposta = requests.get(
        f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios",
        timeout=30,
        verify=False,
    )

    if resposta.status_code == 200:
        municipios = resposta.json()
        print(f"Municípios da UF {uf}:")
        for municipio in municipios:
            print(municipio['nome'])
    else:
        raise Exception(f"Erro na requisição: {resposta.status_code}")
except Exception as e:
    print(e)