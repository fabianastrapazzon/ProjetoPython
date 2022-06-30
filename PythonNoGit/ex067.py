#67 - Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o números solicitado for negativo.

n = 0
while True:
    print('--'*26)
    n = int(input('Digite o número que dejesa conhecer a tabuada: '))
    if n < 0:
        break
    print('--' * 26)
    print(f'TABUADA DO {n}')
    for c in range (0, 10):
        print(f'{c} x {n} = {n*c}')

print('Sessão encerrada')