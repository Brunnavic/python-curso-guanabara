# Condição aninhada = (Uma dentro da outra)
# elif = senão se
# in = procura dentro do que coloquei 

'''
nome = str(input("Digite seu nome:"))
if nome == 'Brunna':
    print("Que nome lindo você tem!")
elif nome in 'Valentina, Sofia, Isabella, Ana':
    print("Seu nome é de uma geração nova!")
else:
    print("Seu nome é normal.")
print("Bom dia, {}!".format(nome))
'''    

# Desafio 036
# Escreva um programa para aprovar o empréstimo
# bancário para a compra de uma casa. O programa vai perguntar
# O VALOR da casa, O SALÁRIO do comprador, e EM QUANTOS ANOS ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% d0 salário,
# ou então o empréstimo será negado.

'''
casa = float(input("Qual é o valor da casa que você quer comprar?:"))
salario = float(input("Qual é o valor do seu salário?:"))
tempo = float(input("Em quantos anos você quer pagar?"))
ano = int(tempo * 12) 
prestacao = casa / ano

porcentagem = salario * 30 / 100

if prestacao <= porcentagem:
    print("Empréstimo aprovado com sucesso!")
    print("O valor da sua parcela por mês será de R${:.2f}!".format(prestacao))
else:
    print("Empréstimo negado!")
    print("A parcela de R${:.2f} excede 30% do seu salário, que é R${:.2f}.".format(prestacao, porcentagem))
'''

# Desafio037
# Escreva um programa que leia um número inteiro
# qualquer e peça para o usuário escolher qual será
# a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal.

'''
num = int(input("Digite um número inteiro:"))
conversao = int(input("Qual será a base de conversão? Digite 1 para binário, 2 para octal ou 3 para hexadecimal!"))

if conversao == 1:
    num_bin = bin(num)
    print(" O valor que você digitou foi {}, que corresponde á {} em Binário!".format(num, num_bin))
    
elif conversao == 2:
    num_octal = oct(num)
    print("O valor que você digitou foi {}, que corresponde á {} em Octal".format(num, num_octal))
    
elif conversao == 3:
    num_hexadecimal = hex(num)
    print("O valor que você digitou foi {}, que corresponde á {} em Octal".format(num, num_hexadecimal))
'''

# Desafio038
# Escreva um programa que leia dois números inteiros
# e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais.

'''
num1 = int(input("Digite um número inteiro:"))
num2 = int(input("Digite outro valor inteiro:"))

if num1 > num2:
    print("O primeiro número que você digitou é {} e o segundo foi {}, portanto o primeiro número é maior que o segundo!".format(num1, num2))

elif num2 > num1:
    print("O primeiro número que você digitou é {} e o segundo foi {}, portanto o segundo número é maior que o primeiro!".format(num1, num2))

elif num1 == num2:
    print("O primeiro número que você digitou é {} e o segundo foi {}, portanto não existe valor maior, os dois são iguais.".format(num1, num2))
'''    
    
# Desafio039
# Faça um programa que leia o ano de nascimento de um jovem
# e informe de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar
# Se já passou do tempo de alistamento
# Seu programa deverá também mostrar o tempo que falta ou que passou do prazo.


from datetime import datetime

ano = int(input("Qual o ano do seu nascimento?"))
ano_atual = datetime.now().year

idade = ano_atual - ano

if idade < 18:
    tempo_restante = 18 - idade
    print("Você tem {} anos, faltam {} anos para seu alistamento!".format( idade, tempo_restante))
    
    
elif idade > 18:
    tempo_restante = idade - 18
    print(" Você tem {} anos, já passou {} anos do seu alistamento!".format(idade, tempo_restante))


elif idade == 18:
    print("Você tem {} anos, é a hora de se alistar!".format(idade))
