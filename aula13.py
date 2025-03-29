# INTRODUÇÃO A FORMATAÇÀO DE STRING COM F-STRINGS

Nome = "Beatriz Braga"
Altura = 1.53
Peso = 79.60
IMC = Peso/(Altura**2)

# f-strings
Linha_1 = f'{Nome} tem {Altura:.2f} de altura' # ao colocar f já tem a possbilidade de colocar variaveis nessa string
Linha_2 = f'pesa {Peso} quilos e seu IMC é {IMC:.2f}'

print(Linha_1)
print(Linha_2)