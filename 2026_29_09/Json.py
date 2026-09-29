#json
#Pra tratar arquivos json o python possui uma biblioteca nativa chamada json.

#Arquivos json sao textos estruturados

pessoa = {"nome": "Joao", "idade": 30, "hobbies": ['caminhada', 'tenis']}
print(type(pessoa)) #<class 'dict'>
print(pessoa) #{'nome': 'João', 'idade': 30, 'hobbies': ['caminhada', 'tenis']}

#a biblioteca json pega esse dicionario e transformar num texto.
#é de suma importancia na hora que se grava o arquivo json, precisar de um texto.

import json
import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def salvar_json(nome_arquivo, dados):
    caminho = BASE_DIR / nome_arquivo
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
    print(f'Arquivo salvo em: {caminho}')

pessoa2 = json.dumps(pessoa) #dumps transforma o dicionario em texto
print(type(pessoa2)) #<class 'str'>
print(pessoa2) #{"nome": "João", "idade": 30, "hobbies": ["caminhada", "tenis"]}

#o uso no entanto é gravar informacoes em um arquivo json. 
#O metodo agora muda de nome: dumps -> dump

salvar_json('alunos.json', pessoa)

#acentuacao e caracteres especiais
pessoanova = {"nome": "João Alvares", "idade": 43, "hobbies": ['caçada de formiga', 'tênis']}
print('com o parametro ensure_ascii=False')
pessoanova2 = json.dumps(pessoanova,indent=4, ensure_ascii=False) #ensure_ascii=False permite que caracteres especiais sejam gravados no arquivo json
print(type(pessoanova2)) #<class 'str'>
print(pessoanova2) #{"nome": "João Alvares", "idade": 43, "hobbies": ["caçada de formiga", "tênis"]}

pessoanova = {"nome": "João Alvares", "idade": 43, "hobbies": ['caçada de formiga', 'tênis']}
print('sem o parametro ensure_ascii=False')
pessoanova2 = json.dumps(pessoanova,indent=4) 
print(pessoanova2) 

salvar_json('alunos.json', pessoanova)

aluns = {
    139219884:{"nome": "João Alvares", "idade": 43, "hobbies": ['caçada de formiga', 'tênis']},
    139219885:{"nome": "Moitinha", "idade": 18, "hobbies": ['bater em idosos', 'futvolei']},
}

salvar_json('todosalunos.json', aluns)


with open(BASE_DIR / 'todosalunos.json', 'r', encoding='utf-8') as arqTodosAlunos:
    dados = json.load(arqTodosAlunos)
    print(dados)

print('\n\nLeitura JSON')

pessoatexto = '{"nome": "João Alvares", "idade": 43, "hobbies": ["caçada de formiga", "tênis"]}'
print(type(pessoatexto)) #<class 'str'>
print(pessoatexto) #{"nome": "João Alvares", "idade": 43, "hobbies": ["caçada de formiga", "tênis"]}
#o metodo loads transforma o texto em dicionario
pessoatexto2 = json.loads(pessoatexto)
print(type(pessoatexto2)) #<class 'dict'>
print(pessoatexto2) #{'nome': 'João Alvares', 'idade': 43, 'hobbies': ['caçada de formiga', 'tênis']}

#como ler de um arquivo json metodo load
with open(BASE_DIR / 'alunos.json', 'r', encoding='utf-8') as arqAluno:
    aluno = json.load(arqAluno)
    print(type(aluno)) #<class 'dict'>
    print(aluno) #{'nome': 'João Alvares', 'idade': 43, 'hobbies': ['caçada de formiga', 'tênis']}


def txt_para_json(caminho_txt, caminho_json):
    registros = []

    with open(caminho_txt, 'r', encoding='utf-8', newline='') as arquivo_txt:
        leitor = csv.reader(arquivo_txt)

        for linha in leitor:
            if not linha:
                continue

            registro = {
                'matricula': linha[0],
                'nome': linha[1],
                'notas': [float(nota) for nota in linha[2:]],
            }
            registros.append(registro)

    with open(caminho_json, 'w', encoding='utf-8') as arquivo_json:
        json.dump(registros, arquivo_json, indent=4, ensure_ascii=False)

    print(f'JSON gerado em: {caminho_json}')


txt_para_json(BASE_DIR / 'exercicios' / 'notas.txt', BASE_DIR / 'exercicios' / 'notas.json')