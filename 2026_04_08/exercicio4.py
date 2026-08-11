#Exercício 04
#Implemente a função media, que recebe três valores numéricos e retorna a média aritmética dos
#valores

def media(num1, num2, num3) -> float:
    return (num1 + num2 + num3) / 3
while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        num3 = float(input("Digite o terceiro número: "))
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
print(f'A média aritmética é: {media(num1, num2, num3)}')

