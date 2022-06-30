#53. Crie um programa que leia uma frase qualquer e diga se ele é um palíndromo, desconsiderando os espaços.
#Ex. Após a sopa.

frase = str(input('Informe a frase que sedeja saber se é um palindromo: ')).strip().lower()
unir = frase.replace(' ','')
palindromo = unir[:: -1]
if unir == palindromo:
    print('A frase "{}" é um palindromo, ela pode ser lida de trás para frente que terá o mesmo significado "{}"'.format(frase,palindromo))
else:
    print('A frase "{}" não é um palindromo pois a sua leitura de tras para frente fica {}'.format(frase,palindromo))

#Usando o FOR
frase2 = str(input('Digite uma frase: ')).strip().upper()
palavra = frase2.replace(' ','')
inverso = ''
for a in range(len(palavra)-1, -1, -1):
    inverso += palavra[a]
print('O inverso de {} é {}'.format(palavra,inverso))
if palavra == inverso:
    print('Por isso é um palindormo')
else:
    print('Por isso não é um palindromo')


