#59. Crie um programa que leia dois valores e mostre um menu no tela:
#[1] Somar
#[2] Multiplicar
#[3] Maior
#[4] Novos números
#[5] Sair do Programa
#Seu programa deverá realizar a apresentação solicitada em cada caso.


soma = 0
mul = 0
maior = 0
op = 1
#for c in range(1,3):
#  n1 = float(input('Informe o {}º número: '.format(c)))
n1 = float(input('Informe o 1º número: '))
n2 = float(input('Informe o 2º número: '))
while op != 5:

    print('''De acordo com os codigos do MENU informe o que deseja realizar
                   [1] SOMAR
                   [2] MULTIPLICAR
                   [3] MAIOR
                   [4] NOVOS NÚMEROS
                   [5] SAIR DO PROGRAMA''')
    op = int(input('>>>> Qual a opção desejada? '))
    if op == 1:
        soma = n1+n2
        print('A soma dos números {} e {} é igual a {}'.format(n1, n2, soma))
        print('==|'*20)
    elif op == 2:
        mul = n1*n2
        print('O produto dos números {} e {} é igual a {}'.format(n1,n2,mul))
        print('==|'*20)
    elif op == 3:
        if n1 < n2:
            print('O maior número informado foi {}'. format(n2))
            print('==|'*20)
        else:
            print('O maior número informado foi {}'.format(n1))
            print('==|')
    elif op == 4:
        print("Informe os novos números que deseja operar")
        n1 = float(input('1º número: '))
        n2 = float(input("2º número: "))
        print('==|'*20)
    elif op == 5:
        print('Finalizando!')


    else:
        print('Código errado!')
        print('==|'*20)
print('Menu encerrado!')
print("------FIM------")