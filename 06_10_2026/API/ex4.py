#Solicite ao usuário um par de moedas (ex.: 
#USD-BRL, EUR-BRL
#) e utilize a API pública de cotações AwesomeAPI para exibir o nome da moeda e os valores de compra 
#valor de compra bid, valor de venda ask.

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def pedir_par_moedas():
    while True:
        par = input("Digite o par de moedas (ex.: USD-BRL, EUR-BRL): ").strip().upper()

        if "-" not in par:
            print("Formato inválido. Use o padrão: CODIGO1-CODIGO2")
            continue

        moedas = par.split("-")
        if len(moedas) != 2 or not all(m.isalpha() and len(m) == 3 for m in moedas):
            print("Formato inválido. Use 3 letras para cada moeda, como USD-BRL.")
            continue

        return "-".join(moedas)


try:
    par_moedas = pedir_par_moedas()
    resposta = requests.get(
        f"https://economia.awesomeapi.com.br/json/last/{par_moedas}",
        timeout=30,
        verify=False,
    )

    if resposta.status_code == 200:
        dados = resposta.json()
        chave = par_moedas.replace("-", "")

        if chave in dados:
            moeda_info = dados[chave]
            nome_moeda = moeda_info.get('name', 'Moeda não informada')
            valor_compra = moeda_info.get('bid', 'N/A')
            valor_venda = moeda_info.get('ask', 'N/A')

            print(f"\nPar consultado: {par_moedas}")
            print(f"Nome da moeda: {nome_moeda}")
            print(f"Valor de compra (bid): {valor_compra}")
            print(f"Valor de venda (ask): {valor_venda}")
        else:
            print(f"Par de moedas '{par_moedas}' não encontrado na API.")
    else:
        raise Exception(f"Erro na requisição: {resposta.status_code}")
except Exception as e:
    print(e)
