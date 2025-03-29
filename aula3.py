# INTRODUÇÃO AOS TIPOS DE DADOS

"""
DocString
Python = Linguagem de programação
Tipo de tipagem = Dinâmica / Forte
str -> string -> texto
Strings são textos que estão dentro de aspas
"""

'''
Tipagem dinâmica significa que o Python já sabe qual é o tipo da informação que vc está passando para ele
Tipagem forte significa que o Python identifica erros de tipo
'''

print(1234) # O Python já sabe que o argumento é um int

# O print necessita de aspas (simples ou duplas) para texto

# Aspas simples
print('Caio Henrique')
print(1, 'Caio "Henrique"')

# Aspas duplas
print("Caio Henrique")
print(2, "Caio 'Henrique'")

# Escape
print("Caio \"Henrique\"") # Não interpreta o caracter depois do \, assim esse caracter é "pulado"

# r
print(r"Caio \"Henrique\"") # Se vc quiser que apareça a \, se usa o r antes para imprimir tudo dentro das aspas