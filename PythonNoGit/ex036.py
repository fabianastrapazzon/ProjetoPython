#36. Escreva um programa para aprovar o empréstimo bancário
# para a compra de uma casa. O programa vai perguntar o
# valor da casa, o salário do comprador e em quantos anos
# ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não
# pode exceder 30% do salário ou então o empréstimo será
# negado.

import pandas as pd

nome = str (input('Informe o seu nome: '))
casa = float(input('Qual o valor da casa que você deseja financiar? '))
salario = float(input('Qual a sua renda? '))
tempo = int(input('Em quantos meses pretende parcelar o pagamento do financeamento? '))

limite = salario*0.30
parcela = casa/tempo
print('Para pagar uma casa no valor de R$ {:.2f} em {} meses'.format(casa,tempo), end = " ")
print('A prestação mesnal será de R$ {:.2f}'.format(parcela))
if parcela > limite:
    print('Olá senhor(a) {} infelizmente o seu emprestimo não foi aprovado pois a sua renda mensal não se enquadra em nossos criteiros de aprovação!'.format(nome))
else:
    print('Olá senhor(a) {} o seu emprestimo foi aprovado!'.format(nome))