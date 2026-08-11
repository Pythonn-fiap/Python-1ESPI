#Exercício 05
#Implemente a função calcular_salario, que recebe o salário atual de um funcionário e retorna o
#salário com um reajuste de aumento, sendo que:
#- Caso o salário seja maior que R$ 2.000,00, o funcionário receberá 7% de aumento.
#- Caso contrário, o funcionário receberá 15% de aumento.

def calcular_salario(salario_atual: float) -> float:
    if salario_atual > 2000:
        return salario_atual * 1.07
    else:
        return salario_atual * 1.15
    
salario_atual = float(input("Digite o salário atual do funcionário: "))
print(f'O salário reajustado é: {calcular_salario(salario_atual)}')

