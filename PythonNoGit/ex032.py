#32. Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
ano = int(input('Informe o ano que deseja sabe se é bissexto ou não. Para saber se o presente ano é Bissesxto difite 0: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é um ano bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))

