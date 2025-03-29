# PRINT

print(12, 34) # Quando a função print tem mais de um argumento, ela imprimi os dois argumetos separados por um espaço
print(56, 78) # O print já faz a quebra de linha
# A quebra de linha padrão do windows é \r\n --> CRLF 

# É possivel mudar o separador do print usando sep
print(12, 34, sep=" - ") # Ao invés de espaço, o seprador é -
print(56, 78, sep=' --> ') # Ao invés de espaçó o separador é -->

# É possivel mudar como será o final do print, se vai ter quebra de linha, usando a argumento end
print(12, 34, sep=" - ", end='\n##\n') # Ele faz mais a quebra de linha (\n), coloca a ## e depois faz quebraa de linha novamente
print(56, 78, sep=' --> ', end='##') # Ele não faz mais a quebra de linha, coloca somente a ## 


# Texto precisa de aspas

# OBS: O Python diferencia letra maiusculas de minusculas