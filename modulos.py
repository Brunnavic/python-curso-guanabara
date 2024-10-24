 
#Usando a biblioteca math de matemática para usar o sqrt de raiz quadrada.
'''
from math import sqrt
num = int(input('Digite um número:'))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))
'''
#Usando a biblioteca random para mostrar um número aleatório.
'''
import random
num = random.randint(1,10)
print(num)
'''
#Usando a biblioteca que precisei instalar de emoji para mostrar um emoji.
# instalação: pip install emoji
'''
import emoji

print(emoji.emojize("Olá mundo :globe_showing_Americas:"))
'''
#Desafio 016

    #Crie um programa que leia um número Real
    #qualquer pelo teclado e mostre na tela a sua 
    #porção inteira. EX: 6.127 o número 6.127 tem a 
    #parte inteira 6.
'''
import math
num = float((input('Digite um número ')))
int = math.trunc(num)
print('A parte inteira de {} é {} '.format(num, int ))
'''

#Desafio 017

    #Faça um programa que leia o comprimento
    #do cateto oposto e do cateto adjacente de
    #um triangulo retangulo, calcule e mostre 
    #o comprimento da hipotenusa.
'''
import math
cateto_oposto = float(input('Digite o comprimento do cateto oposto '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente'))
soma = (cateto_oposto * cateto_oposto) + (cateto_adjacente * cateto_adjacente)
hipotenusa =  math.sqrt (soma)

print('O cateto oposto é {}, e o cateto adjacente é {}, portanto o resultado da hipotenusa é {:.2f}'.format(cateto_oposto, cateto_adjacente, hipotenusa))
'''


#Desafio 18

    #Faça um programa que leia 
    #um Ângulo qualquer e mostre na tela o valor
    #do seno, cosseno e tangente desse Ângulo.
'''
import math
angulo = float(input('Qual o seu angulo?'))
rad = math.radians(angulo)
seno = math.sin(rad)
cose = math.cos(rad)
tang = math.tan(rad)

print('O seu angulo é{}, o seno é{:.2f} o cosseno é {:.2f} e tangente é{:.2f}'.format(angulo, seno,cose,tang))

'''
#Desafio 019

    #Um professor quer sortear
    #um dos seus quatro alunos 
    #para apagar o quadro. Faça um 
    #programa que ajude ele, lendo o nome 
    #deles e escrevendo o nome do escolhido.
'''
import random

alunoA = input('digite seu nome:')
alunoB = input('digite seu nome:')
alunoC = input('digite seu nome:')
alunoD = input('digite seu nome:')

sorteio = [alunoA, alunoB, alunoC, alunoD]
escolhido = random.choice(sorteio)

print('O professor tem esses alunos:{},{},{},{} mas o escolhido foi {}'.format(alunoA,alunoB,alunoC,alunoD,escolhido))

'''
#Desafio 020

    #O mesmo professor do desafio
    #anterior quer sortear a ordem 
    #de apresentação de trabalhos dos alunos
    #Faça um programa que leia o nome dos quatro
    #alunos e mostre a ordem sorteada.

'''
import random

alunoA = input('digite seu nome:')
alunoB = input('digite seu nome:')
alunoC = input('digite seu nome:')
alunoD = input('digite seu nome:')

sorteio = [alunoA, alunoB, alunoC, alunoD]
random.shuffle(sorteio)
print('A ordem de apresentação será:')
print(sorteio)
'''


#Desafio21
    #Faça um programa que abra
    #e reproduza um arquivo de áudio MP3.
'''
import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
'''


