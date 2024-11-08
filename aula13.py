
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

s = 0

for index in range(1, 501,):
    if index % 2 == 1:
        impar = index
        if impar % 3 == 0:
            s = s + impar
            
print(s)   




