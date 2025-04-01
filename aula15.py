#INPUT

nome = input('Qual o seu nome? \n')
print(f'O seu nome é {nome}')
print(f'{nome=}') # Imprimi nome = O valor do nome

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

#Necessario transformar em inteiros, pois o input recebe STR, e se somar STR ocorre contatenação
int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')