#41. A confederação Nacional de Natação precisa de um
# programa que leia o ano de nascimento de um atleta e
# mostre sua categoria de acordo com a idade:
#- Até 9 anos: Mirim
#- Até 14 anos: Infantil
#- Até 19 anos: Júnior
#- Até 20 anos: Sênior
#- Acima: Máster

from datetime import date

ano = int(input('Informe o seu ano de nascimento: '))
atual = date.today().year
idade = atual - ano
if idade < 10:
    print('Você tem {} anos, a sua categoria de seleção é Mirim.'. format(idade))
elif idade < 15:
    print('Você tem {} anos, a sua categoria é Infatil.'.format(idade))
elif idade < 20:
    print('Você tem {} anos, a sua categoria é Júnior.'.format(idade))
elif idade < 21:
    print('Você tem {} anos, a sua categoria é Sênior.'.format(idade))
else :
    print('Você tem {} anos, a sua categoria é Máster.'.format(idade))