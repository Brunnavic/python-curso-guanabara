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


