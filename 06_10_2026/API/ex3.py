#A API abaixo retorna um JSON com informações de 50 receitas culinárias. Faça um
#programa que consulte a API e exiba todas as receitas que utilizam um determinado
#ingrediente informado pelo usuário.

import requests

try:
    receita = input("Digite o ingrediente que deseja buscar nas receitas: ").strip().lower()
    resposta = requests.get("http://dummyjson.com/recipes?limit=50")
    if resposta.status_code == 200:
        dados = resposta.json()
        receitas = dados['recipes']
        receitas_filtradas = [r for r in receitas if receita in r['ingredients']]
        
        if receitas_filtradas:
            print(f"Receitas que utilizam o ingrediente '{receita}':")
            for r in receitas_filtradas:
                print(f"- {r['title']}")
        else:
            print(f"Nenhuma receita encontrada com o ingrediente '{receita}'.")
    else:
        raise Exception(f"Erro na requisição: {resposta.status_code}")
except Exception as e:
    print(e)
