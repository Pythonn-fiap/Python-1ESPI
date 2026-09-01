# Exercício 8 Represente uma tabela de notas de 3 alunos, em 3 disciplinas cada, como uma tupla de
# tuplas (uma "matriz imutável"): notas = ((7.0, 8.5, 6.0), (9.0, 7.5, 8.0), (5.5, 6.5, 7.0)) . Escreva
# uma função media_aluno que receba essa tupla de tuplas e o índice de um aluno, e retorne a média das
# notas desse aluno
 
def media_aluno(notas, indice_aluno):
    if indice_aluno < 0 or indice_aluno >= len(notas):
        return "Índice de aluno inválido"
   
    notas_aluno = notas[indice_aluno]
    media = sum(notas_aluno) / len(notas_aluno)
    return media
print(f'Média do aluno 1: {media_aluno(((7.0, 8.5, 6.0), (9.0, 7.5, 8.0), (5.5, 6.5, 7.0)), 0):.2f}')
print(f'Média do aluno 2: {media_aluno(((7.0, 8.5, 6.0), (9.0, 7.5, 8.0), (5.5, 6.5, 7.0)), 1):.2f}')
print(f'Média do aluno 3: {media_aluno(((7.0, 8.5, 6.0), (9.0, 7.5, 8.0), (5.5, 6.5, 7.0)), 2):.2f}')