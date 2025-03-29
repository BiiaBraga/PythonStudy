# INTRODUÇÃO AOS TIPOS DE DADOS

# Tipos int e float

# int -> Número inteiro
# O tipo int representa qualquer número positivo ou negativo. 
# int sem sinal é considerado positivo.
print("Testando inteiro")
print(11) # int
print(-11) # int
print(0)
print(end='\n')

# float -> Número com ponto flutuante
# O tipo float representa qualquer número positivo ou negativo com ponto flutuante.
# float sem sinal é considerado positivo.
# float usa . e não ,
print("Testando float")
print(1.1, 10.11)
print(0.0, -1.5) 
print(end='\n')

# A função type mostra o tipo que o Python inferiu ao valor.
print("Testando a função type") # type, aliás, não é uma funçào e sim uma classe
print(type('Amanda')) # texto é string, em python str
print(type(0))
print(type(1.1), type(-1.1), type(0.0))

# OBS: para comentar e descomentar várias linhas de uma vez, só selecionar as linhas e usar crtl+/
# obs: tudo em python é um objeto