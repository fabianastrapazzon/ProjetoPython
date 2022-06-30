#45. Crie um programa que faça o computador jogar
# Jokenpô com você

import random
import time

print('Vamos jogar Jokempô???')
time.sleep(2)
print('Vamos lá\n'
      'Regras do jogo:\n'
      'A pedra quebra a tesoura.\n'
      'A tesoura corta o papel.\n'
      'O papel embrulha a pedra.\n\n')
#time.sleep(2)
usuario = str(input('ESCOLHA A SUA ARMAAAA\n'
                    'PEDRA\n'
                    'PAPEL\n'
                    'TESOURA\n'
                    '.... ')).strip().lower()
print('Jo')
time.sleep(1)
print('Ken')
time.sleep(1)
print('Pô')
time.sleep(1)
lista = ['tesoura','papel','pedra']
computador = random.choice(lista)
if usuario == 'pedra' and computador== 'tesoura':
    print('Parabéns, você ganhou, eu escolhi {}'.format(computador))
elif usuario == 'tesoura' and computador == 'papel':
    print('Parabéns, você ganhou, eu escolhi {}'.format(computador))
elif usuario == 'papel' and computador == 'pedra':
    print('Parabéns, você ganhou, eu escolhi {}'.format(computador))
elif usuario == 'tesoura' and computador == 'tesoura' or usuario == 'papel' and computador == 'papel' or usuario == 'pedra' and computador =='pedra':
    print('Oraa, eu também escolhi {}. Vamos de novo??'.format(computador))
else:
    print('Você Perdeu, eu escolhi {}'.format(computador))

