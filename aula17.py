# CONTINUIÇAO IF / ELIF/ ELSE

condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = True


if condicao1:
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
    pass #Passa/pula
elif condicao3:
    print('Código para condição 3')
elif condicao4:  # Essa condição não é nem verificada, pois a condição 3 entrou no seu bloco
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita')

if 10==10:
    print('Outro if')

print('Fora do if')