import json
import os

def ler_heroes(heroes):
    if not os.path.isfile(heroes):
        raise FileNotFoundError(f"Arquivo não encontrado: {heroes}")

    try:
        with open(heroes, "r", encoding="utf-8") as f:
            dados = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Erro ao decodificar JSON: {e}")

    # Se o JSON for uma lista de heróis
    if isinstance(dados, list):
        for heroi in dados:
            nome = heroi.get("name")
            poderes = heroi.get("powers", [])
            print(f"Nome: {nome}")
            print("Poderes:", ", ".join(poderes) if poderes else "Nenhum poder listado")
            print("-" * 40)

    # Se o JSON for um objeto com a lista de membros
    elif isinstance(dados, dict):
        membros = dados.get("members", [])

        if isinstance(membros, list):
            for heroi in membros:
                nome = heroi.get("name")
                poderes = heroi.get("powers", [])
                print(f"Nome: {nome}")
                print("Poderes:", ", ".join(poderes) if poderes else "Nenhum poder listado")
                print("-" * 40)
        else:
            nome = dados.get("name")
            poderes = dados.get("powers", [])
            print(f"Nome: {nome}")
            print("Poderes:", ", ".join(poderes) if poderes else "Nenhum poder listado")
    else:
        print("Formato de JSON não reconhecido.")

if __name__ == "__main__":
    ler_heroes("heroes.json")