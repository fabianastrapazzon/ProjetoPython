#71 - Crie um programa que simule o funcinamento de um caixa eletrônico. No inicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas célular de cada valor serão entregues.
#Obs: Considere  que o caixa possuiu cédulas de R$50,00; R$20,00; R$10,00 e R$1,00
print('{:=^40}'.format('Banco CEV'))
saque = int(input('Qual o valor que deseja sacar? R$'))
n20 = n10 = n50 = n1 = 0

resul = saque
while True:
    if saque >= 50:
        n50 = saque//50
        saque = saque % 50

    if saque >= 20:
        n20 = saque//20
        saque = saque % 20

    if saque >= 10:
        n10 = saque // 10
        saque = saque % 10

    if 0 < saque < 10:
        n1 = saque/1
        saque = saque - n1
    if saque == 0:
        break
print(f'Você solicitou um saque de R${resul} e irá receber em:\n'
      f'{n50} notas de R$50,00\n'
      f'{n20} notas de R$20,00\n'
      f'{n10} notas de R$10,00\n'
      f'{n1:.0f} notas de R$1,00')

