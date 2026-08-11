def calcular_dissidio( salario:float, percentual:float = 0.08) -> float:
    if percentual <1:
        percentual = percentual / 100
    salario_aumento = salario * (1+ percentual)
    return salario_aumento

salario_atual = 10000
print(f'com o dissidio o seu salario passou de R${salario_atual} para'
      f'R${calcular_dissidio(salario=salario_atual,percentual=0.5)}')
#nao passa o percentual de aumento e usa o valor default
