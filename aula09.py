#Manipulando textos 
'''
frase = 'Curso em video Python'
print(frase[2:13])
print(frase.count ('o'))
print(len(frase))
print(frase.replace('Curso', 'Aprendendo'))
print('Curso' in frase)
'''

#Exercicios
#Desafio022

    #Crie um programa que leia
    #o nome completo de uma pessoa
    #e mostre:

    #O nome com todas as letras maiusculas:
'''nome = input('digite seu nome completo:')
print(nome.upper())'''
    #O nome com todas minusculas
'''nome = input('Digite seu nome:')
print(nome.lower())'''
    #Quantas letras ao todo sem considerar espaços
'''nome = input('Digite seu nome:')
nome_com_es = (nome.split())
nome_sem_es = (''.join(nome_com_es))'''

#quantidade letra sem espaço
'''print(len(nome_sem_es))'''
#quantidade letra com espaço
'''print(len(nome))'''

#Quantas letras tem o primeiro nome
'''nome = input('Digite seu nome:')
nome_com_es = (nome.split())
print(len(nome_com_es [0]))'''


#Desafio023

    #Faça um programa que leia um número
    #de 0 a 9999 e mostre na tela cada um dos
    #dígitos separados.EX: Digite um número:1834
    #unidade:4
    #dezena:3
    #centena:8
    #milhar:1
'''
num = int((input('Digite um número:')))
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mi = num // 1000 % 10
print('Seu número é: {} \n unidade: {}\n dezena: {}\n centena: {}\n milhar: {}'.format(num,uni,dez,cen,mi))
'''

#Desafio024

    #Crie um programa que leia
    #o nome de uma cidade e diga se ela começa
    #ou não com o nome 'SANTO'.
'''
cidade = input('Digite o nome da sua cidade:')
separado = cidade.split() 

print( separado[0].upper() == 'SANTO' )
'''
#Desafio025
    #Crie um programa que leia
    #o nome de uma pessoa e diga
    #se ela tem "Silva" no nome.
'''
nome = str(input('Digite seu nome completo:')).strip()
print( 'SILVA' in nome.upper() )'''

#Desafio026
    #Faça um programa que leia uma frase
    #pelo teclado e mostre:
#Quantas vezes aparece a letra 'a'.
'''
frase = input('Digite sua frase:')
contar = frase.upper() .count('A')
print(contar)'''
#Em qual posição ela aparece a primeira vez.
'''
frase = input('Digite sua frase:')
posi = frase.upper .find('A')
print(posi)'''

#Em qual posição ela aparecea ultima vez.
'''
frase = input('Digite sua frase:')
posi = frase.upper .find('A' [0:-1])
print(posi)'''




#Desafio027
    #Faça um programa que leia o nome completo de uma pessoa
    #mostrando em seguida o primeiro e o ultimo nome separadamente.
    #EX: Ana Maria Souza
    #primeiro: Ana
    #ultimo: Souza
'''
nome = input('Digite seu nome completo:')
separado = nome.split() 
print('Primeiro nome:{}'.format(separado [0]))
print('último nome: {}'.format(separado [-1]))
'''











