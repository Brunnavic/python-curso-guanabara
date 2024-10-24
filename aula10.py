#Condições 
'''
nome = str(input("Qual seu nome?")) 
if nome == 'BRUNNA':
    print("Que nome lindo o seu!!")
print("Bom dia,{}!".format(nome))
'''

'''
nota1 = float(input("Digite sua nota de Português:")) 
nota2 = float(input("Digite sua nota de Matemática:"))
media = (nota1 + nota2 / 2)

if media <=6:
    print("Sua média é {:.1f}, e está baixa, estude mais!".format(media))
else:
    print("Sua média é {:.1f} e está alta, parabéns!".format(media))
'''

#Desafio028
    # Escreva um programa que faça o computador pensar
    # em um número  inteiro entre 0 e 5, e peça para o
    # usuário tentar descobrir qual foi o número escolhido pelo 
    # computador. O programa deverá mostrar na tela se o usuário
    # perdeu ou ganhou.
    
'''
import random
from time import sleep
  
frase = int(input("Pensei em um número entre 0 e 5, adivinhe qual é?"))
lista = [0, 1, 2, 3, 4, 5] 
sorteio = random.choice(lista)

print("PROCESSANDO...")
sleep(2)

if sorteio == frase:
    print("CERTA RESPOSTA :) ")
    print("O número que eu pensei foi: {}, e o número que vc escolheu foi {}, portanto vc ACERTOU!".format(sorteio, frase))
else:
    print("ERROU :( ")
    print("O número que eu pensei foi: {}, e o número que vc escolheu foi {}, portanto vc ERROU!".format(sorteio, frase))
'''

#Desafio029
    # Escreva um programa que leia a velocidade de um carro.
    # se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado!
    # A multa vai custar R$07,00 reais por cada km á cima do limite.
    
'''  
carros = int(input("Em qual volocidade em km/h você está?"))
limite = 80
multaKM = 7 

if carros > limite:
    acima = carros - limite
    multa = acima * multaKM
    print("Você está á {} km/h ,ultrapassou 80km/h, portanto foi multado!".format(carros))
    print("E a multa é de R${},00".format(multa))
'''

#Desafio030
    # Crie um programa que leia um número inteiro na tela 
    # e mostre se ele é par ou impar!
    # Obs:Para saber se é impar ou par devemos dividir por 2
    
'''    
num = int(input("Digite um número inteiro:"))    
par = (num % 2 == 0)
impar = (num % 2 == 1)

if par:
    print(num)
    print("Seu número é par!")
else:
    print(num)
    print("Seu número é ímpar")
'''

#Desafio031
    #Desenvolva um programa que pergunte a distância de uma
    # viagem em km. Calcule o preço da passagem cobrando R$0,50 por km para 
    # viagens de até 200km e R$0,45 por km para viagens mais longas.
    
'''   
viagem = float(input("Qual a distância em km da sua viagem?"))

distancia = 200
preçoKMCaro = 0.50
preçoKMBarato = 0.45

if viagem <= distancia:
    preço = viagem * preçoKMCaro
    print(" O preço da sua viagem é R${:.2f}".format(preço))
    
else:
    preço = viagem * preçoKMBarato
    print(" O preço da sua viagem é R${:.2f}".format(preço))
   
'''
    
#Desafio032
    #Desenvolva um programa que leia um ano qualquer e veja 
    # se ele é Bissexto.
    
#Bissexto: Se o ano é divisível por 4, e não é divisível por 100, ou se é divisível por 400.
#Não bissexto: Se o ano é divisível por 100, mas não por 400, ou se não é divisível por 4.

'''
from datetime import date

ano = int(input("Digite um ano ou coloque 0 para analisar o ano atual:"))
if ano == 0:
    ano = date.today().year
    
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print( ano, "é bi")
else:
    print( ano, "Não é um ano bissexto")
'''

#Desafio033
    # Faça um programa que mostre 3 números e mostre 
    # qual é o maior e qual é o menor.
    
'''   
num1 = int(input("Digite o primeiro número inteiro:"))
num2 = int(input("Digite o segundo número inteiro:"))
num3 = int(input("Digite o terceiro número inteiro:"))

numeros = [num1, num2, num3]
print(numeros)
    
maiornum = max(numeros)
menornum = min(numeros)
print(" O número maior é: {} e o número menor é: {}".format(maiornum, menornum))
'''

#Desafio034
    # Desenvolva um programa que pergunte o salário de um 
    # funcionário, e calcule o valor do seu aumento. Para salários
    # acima de R$1.250,00 calcule um aumento de 10%. Para salários inferiores
    # ou menores o aumento é de 15%!

'''  
salario = float(input("Qual o seu salário?")) 
porcentagem10 = (salario * 10 ) / 100
porcentagem15 = (salario * 15) / 100

if salario <= 1250:
    aumento15 = salario + porcentagem15
    print(" O salário com o aumento de 15% passa a ser: R${},00".format(aumento15))
else:
    aumento10 = salario + porcentagem10
    print(" O salário com o aumento de 10% passa a ser: R${},00".format(aumento10))
'''


#Desafio035
    # Faça um programa que mostre o comprimento de 3 retas e
    # diga ao usuário se elas podem ou não formar um triângulo.
        
'''      
reta1 = float(input("Digite o tamanho da reta 1: "))
reta2 = float(input("Digite o tamanho da reta 2: "))
reta3 = float(input("Digite o tamanho da reta 3: "))

# Verifica se as três condições da desigualdade triangular são verdadeiras
if (reta1 + reta2 > reta3) and (reta1 + reta3 > reta2) and (reta2 + reta3 > reta1):
    print("Pode ser um triângulo")
else:
    print("Não pode ser um triângulo")
    
'''

