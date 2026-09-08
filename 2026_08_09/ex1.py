#reencha um dicionário com as informações de 5 pessoas. Utilize o CPF da pessoa como chave e o
#nome como valor. Solicite os dados ao usuário.

pessoas = {}

for i in range(5):
    cpf = input(f"Informe o CPF da {i+1}ª pessoa: ")
    nome = input(f"Informe o nome da {i+1}ª pessoa: ")
    pessoas[cpf] = nome

# Mostrar o dicionário preenchido
print("\nDicionário preenchido:")
for cpf, nome in pessoas.items():
    print(f"CPF: {cpf} -> Nome: {nome}")   