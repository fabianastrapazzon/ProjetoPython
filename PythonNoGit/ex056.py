#56. Desenvolva que leia o NOME, IDADE e SEXO de 4 pessoas. no final do programa, mostre:
#A média de idade do grupo;
#Qual é o nome do homem mais velho;
#Quantas mulheres têm menos de 20 anos.
s = 0
cont = 0
import math
velho = 0
nvelho = 0
for c in range(1,5):
    print("-------- {}ª PESSOA -------".format(c))
    nome = str(input('Informe o seu nome: '))
    idade = int(input('Informe a sua idade: '))
    sexo = int(input('Informe o codigo corrspondente ao seu sexo:\n[1] Feminino\n[2] Masculino\n '))
    s += idade
    if sexo == 1 and idade < 20:
        cont += 1
    if sexo == 2 and c == 1:
        velho = idade
        nvelho = nome
    if idade > velho and sexo == 2:
            nvelho = nome
            velho = idade
print('A média de idade do grupo é {:.2f}'.format(s/4))
print('{} mulheres possuem menos de 20 anos de idade'.format(cont))
print('{} é o homem mais velho e tem {} anos'.format(nvelho,velho))