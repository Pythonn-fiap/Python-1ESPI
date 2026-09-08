#Preencha um dicionário com os dados de 5 alunos. Utilize o RM do aluno como chave e uma lista de
#três notas como valor. Solicite os dados ao usuário. Percorra o dicionário e exiba a média de cada
#aluno.

alunos = {}

for i in range(5):
    rm = input(f"Informe o RM do {i+1}º aluno: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Informe a {j+1}ª nota do {i+1}º aluno: "))
        notas.append(nota)
    alunos[rm] = notas

    #exibe a media

print("\nMédia dos alunos:")
for rm, notas in alunos.items():
    media = sum(notas) / len(notas)
    print(f"RM: {rm} -> Média: {media:.2f}")