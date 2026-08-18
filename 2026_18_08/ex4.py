#Crie uma função (com def , não lambda) chamada para_maiuscula que receba um texto e
#devolva o mesmo texto em letras maiúsculas. Depois, use map para aplicar essa função a
#toda a lista nomes = ["ana", "bruno", "carla"] 

para_maiscula = lambda texto: texto.upper()
nomes = ["ana", "bruno", "carla"]
print(list(map(para_maiscula, nomes)))  # Saída: ['ANA', 'BRUNO', 'CARLA']