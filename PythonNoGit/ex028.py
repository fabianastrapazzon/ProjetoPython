#28. Escreva um programa que faça o computador “pensar” em um número inteiro ente 0 e 5 e peça para
#o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
import time
n = int(input('Advinhe qual o número que estou pensando entre 0 e 5: '))
n1 = random.randint(0,5)
print('========'*10)
print('Aguarde, Processando ......')
time.sleep(3)
print('========'*10)

if n == n1:
    print('Parabéns você acertou, o número em que pensei foi {}'.format(n1))
else:
    print("Você erro, o número que pensei foi {}".format(n1))

