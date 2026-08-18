#Crie uma função lambda chamada par_ou_impar que receba um número inteiro e devolva a
#string "par" se ele for par, ou "ímpar" caso contrário.

par_ou_impar = lambda n: "par" if n % 2 == 0 else "ímpar"
# Testando a função lambda
print(par_ou_impar(4))  # Saída: par
print(par_ou_impar(7))  # Saída: ímpar