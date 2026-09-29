import json
from pathlib import Path

pasta = Path(__file__).resolve().parent
alunos = {}
with open(pasta / 'notas.txt', 'r', encoding='utf-8') as file:
    arqAlunos = file.readlines()
    for linha in arqAlunos:
        linha = linha.strip()
        aluno = linha.split(',')
        rm = aluno[0]
        nome = aluno[1]
        notas_str = aluno[2:]
        notas = [float(nota) for nota in notas_str]
        alunos[rm] = {'nome': nome, 'notas': notas}

print(alunos)
with open(pasta / 'alunos.json', 'w', encoding='utf-8') as arqAlunos:
    json.dump(alunos, arqAlunos, ensure_ascii=False, indent=4)
