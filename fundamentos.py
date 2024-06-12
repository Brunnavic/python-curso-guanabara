'''

print('Olá Mundo!')

nome = input(('Digite seu nome:'))
idade = input(('Digite sua idade:'))
print('Prazer em te conhecer, {}! sua idade é: {}'.format(nome,idade))

'''

'''
nome = 'Brunna'
sobrenome = 'Martins'
sexo = 'feminino 2'

#print('Seu nome é: {}, seu sobrenome é {}, e seu sexo é {}'.format(nome, sobrenome, sexo))

print(nome.isalpha())
print(sobrenome.islower())
print(sexo.isalnum())
'''

'''
algo = input('Digite algo:')

print('O tipo primitivo desse valor é ',type(algo) )

print('Só tem espaço? {}'.format(algo.isspace()))
print('É um número? {}'. format(algo.isnumeric()))
'''

'''
nome = (input('Qual é seu nome?'))
print('Prazer em te conhcer {:20}!'.format(nome))

'''


#Desafio 005

    #Faça um programa que leia um número inteiro 
    #e mostre na tela o seu sucessor e seu antecessor.
'''
num1 = int(input('Digite um número:'))
print('O antecessor desse número é: {} e o sucessor é {}'.format(num1 - 1, num1 + 1))
'''

#Desafio 006

    #Crie um algoritmo que leia um número
    #e mostre o seu dobro, triplo e raiz quadrada.
'''
num1 = int(input('Digie um número:'))

print('O dobro desse número é {}, o triplo é {}, e a raiz quadrada é {}'.format( num1 *2, num1 *3, num1**(1/2)))
'''


#Desafio 007

    #Desenvolva um programa que leia as duas notas
    #de um aluno, calcule e mostre sua média
'''
matematica = float(input('Digite sua nota de Matemática:'))
portugues = float(input('Digite sua nota de Portugês:'))
soma = matematica + portugues
media = soma / 2

print('A média das suas notas é {}'.format(media))
'''

#Desafio 008

    #Escreva um programa que leia um valor 
    #em metros e o exiba convertido em centimetros e milimetros
'''
valor_metro = float(input('Digite um valor em metros:'))
centimetros = valor_metro * 100
milimetros = valor_metro * 1000

print('O valor do metro é {}, ele tem {} centímetros e {} milímetros.'.format(valor_metro, centimetros, milimetros))
'''

#Desafio 009

    #faça um programa que leia um número
    #inteiro qualquer e mostre na tela a sua tabuada.
'''
num1 = int(input('Digite um número:'))
x0 = num1 * 0
x1 = num1 * 1
x2 = num1 * 2
x3 = num1 * 3
x4 = num1 * 4
x5 = num1 * 5
x6 = num1 * 6
x7 = num1 * 7
x8 = num1 * 8
x9 = num1 * 9
x10 = num1 *10

print('=========================')
print('A tabuada de {} é:'.format(num1))
print('{} x 0 = {}'.format(num1, x0))
print('{} x 1 = {}'.format(num1, x1))
print('{} x 2 = {}'.format(num1, x2))
print('{} x 3 = {}'.format(num1, x3))
print('{} x 4 = {}'.format(num1, x4))
print('{} x 5 = {}'.format(num1, x5))
print('{} x 6 = {}'.format(num1, x6))
print('{} x 7 = {}'.format(num1, x7))
print('{} x 8 = {}'.format(num1, x8))
print('{} x 9 = {}'.format(num1, x9))
print('{} x 10 = {}'.format(num1, x10))

#print('A Tabuada desse número é: \n {:<} \n{:<} \n{:<} \n{:<} \n{:<} \n{:<} \n{:<} \n{:<} \n{:<} \n{:<} \n{:<} '.format(x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10))
'''


#Desafio 010

    #Crie um programa que leia quanto dinheiro uma pessoa tem na carteira 
    # e mostre quantos Dólares ela pode comprar.
'''
dolar = 5.17
quantidade = float(input('Quanto você tem na sua carteira?'))
print('Você tem R${:.2f} reais, portanto pode comprar {:.2f} US$Dólares!'.format( quantidade, quantidade / dolar))

'''
#desafio 011
 
    #Faça um programa que leia a altura e a largura
    #de uma parede em metros, calcule a sua área e a 
    #quantidade de tinta necessária para pintá-la, 
    #sabendo que cada litro de tinta pinta uma área de 2m2 (2 metros ao quadrado)
'''
altura = float(input('Digite a altura da sua parede:'))
largura = float(input('Digite a largura da sua parede:'))
area = altura * largura
tinta = 2

print('A área da sua parde é {}, portanto irá precisar de  {} litros de tinta!'.format(area, area / tinta))
'''

#Desafio 012

    #Faça um algoritmo que leia o preço
    #de um  produto e mostre seu novo preço
    #com 5% de desconto.
'''
produto = float(input('Qual o preço do produto?'))
conta = produto * 5 / 100
total_desconto = produto - conta

print('O seu produto custa: R${}, mas com o desconto sai a R${}'. format(produto, total_desconto))
'''

#Desafio 013

    #Faça um algoritmo que leia
    #o salário de um funcionário e 
    #mostre seu novo salário, com 15% 
    #de aumento.
'''
salario = float(input('Qual é o seu salário?'))
conta = salario * 15 / 100
reajuste = salario + conta
print('Seu salário era R${} e passou a valer R${} com o aumento!'.format(salario, reajuste))
'''
#Desafio 014

    #Conversão de temperatura
    #Escreva um programa que converta uma temperatura 
    #digitada em C e converta para F.
'''
temperatura = float(input('Digite a sua temperatura em C'))
conversao = temperatura * 1.8 + 32
print('Sua temperatura {} em Grau Celsius corresponde a {} em Graus Fahrenheit'.format(temperatura, conversao))
'''

#Desafio 015

    #Escreva um programa que pergunte a quantidade de Km percorridos
    #por um carro alugado e a quantidade de dias pelos quais ele foi
    #alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00
    #o dia e R$0,15 por km rodado.

'''
quant_km = float(input('Qual a quantidade de km percorrido?'))
quant_dias = int(input('Qual a quantidade de dias alugado'))
carro = 60
dia = 0.15
preco = (quant_km * dia) + (carro * quant_dias)

print('O Preço do Aluguel ficou R${}'.format(preco))
'''


