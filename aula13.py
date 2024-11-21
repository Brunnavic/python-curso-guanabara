
'''
for index in range(0,4):
    print("Oi")
''' 
# Desafio046

# Faça um programa que mostre na tela
# uma contagem regressiva para o estouro de fogos
# de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''
from time import sleep
import emoji

for index in range(10,0, -1):
    print(index)
    sleep(1) 
print(emoji.emojize("Feliz Ano Novo! :fireworks:"))
'''

# Desafio047

# Crie um programa que mostre todos os números pares
# que estão no intervalo entre 1 e 50.

'''
for index in range(1, 51,):
    if index % 2 == 0:
        print(index)
'''

# Desafio048

# Faça um programa que calcule a soma entre todos os números
# ímpares que são multiplos de 3 e que se encontram no intervalo entre 1 e 500.

# Código que eu fiz:
'''
s = 0

for index in range(1, 501,):
    if index % 2 == 1:
        impar = index
        if impar % 3 == 0:
            s = s + impar
            
print(s) 
  
'''

# Código que olhei no chat depois para ver se a lógica estava correta:
# Obs: Percebi que não precisava olhar se o número era ímpar, apenas pular de 2 em 2 no range

'''
s = 0

# Percorrendo apenas os números ímpares entre 1 e 500
for index in range(1, 501, 2):  # '2' no terceiro parâmetro garante que só percorremos números ímpares
    if index % 3 == 0:  # Verifica se o número é múltiplo de 3
        s += index  # Soma o número à variável 's'

print(s)

'''

# Desafio049

# Refaça o desafio 009, mostrando a tabuada de um número
# que o usuário escolher, só que agora usando o laço for.
'''
num = int(input("Digete o número que você quer saber a tabuada:"))

print("A tabuada de {} é:".format(num))  

for index in range(0,11):
    tabuada = num * index
    #print(tabuada)
    print(num,'X',index,'=', tabuada)
'''

# Desafio050
# Desenvolva um programa que leia 6 números inteiros
# e mostre a soma apenas daqueles que forem pares. Se o valor 
# digitado for ímpar, desconsidere-o.
'''
soma = 0

for index in range(0,6):
    num = int(input("Digite um número inteiro:"))
    if num % 2 == 0:
        soma += num
    
        
print("A soma dos números pares é {}".format(soma))
             
'''

# Desafio051
# Desenvolva um programa que leia o peimeiro termo
# e a razão de uma progressão aritmética. No final mostre os 
# 10 primeiros termos dessa progressão.

'''
termo1 = int(input("Qual o primeiro termo da sua PA?:"))  
razao = int(input("Qual a razão da sua PA?:"))        
progre = termo1                 #Aqui a progre começa com o termo1 porque quero começar a partir do 
                                # número que o usuário digitar e não do 0, como achei no inicio.
for index in range(0,10,):
    progre += razao
    print(progre)       
'''
    
    
    












