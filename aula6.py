#COERSÃO --> CONVERSÃO DE TIPOS

# type convertion, typecasting, coercion é o ato de converter um tipo em outro tipo imutáveL e primitivo:
# str, int, float, bool

# Os códigos abaixo não funcionam, pois não é possivel somar dois tipos diferentes
# print('a' + 1)
# print('1' + 1)

# Já o código abaixo consegue fazer essa soma, pois os tipos dos dados são iguais --> polimorfismo
print(1 + 1)
print('a' + 'b') # somar textos = contatenar

# coersão: colocar o tipo antes do dados que vai mudar de tipo
print(int('1'), type(int('1')))
print(type(float('1') + 1)) # O Python consegue somar um int com um float
print(bool(' ')) # String vazia = False e String com dados (mesmo q seja um espaço) = True
print(str(11) + 'b')