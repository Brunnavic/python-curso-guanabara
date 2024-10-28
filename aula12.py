

nome = str(input("Digite seu nome:"))
if nome == 'Brunna':
    print("Que nome lindo você tem!")
elif nome in 'Valentina, Sofia, Isabella, Ana':
    print("Seu nome é de uma geração nova!")
else:
    print("Seu nome é normal.")
print("Bom dia, {}!".format(nome))
    