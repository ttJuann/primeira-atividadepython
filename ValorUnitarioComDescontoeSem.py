# Mensagem de boas-vindas à loja
print("Bem-vindo(a) à Loja!")


# Pedindo entrada ao usuário
valor_unitario = float(input("Digite o valor unitário do produto: "))  # Solicita ao usuário o valor unitário do produto.
quantidade = int(input("Digite a quantidade do produto: "))  # Solicita ao usuário a quantidade do produto.


# Calculando subtotal
subtotal = valor_unitario * quantidade  # Calcula o subtotal multiplicando o valor unitário pela quantidade.


# Verificando a quantidade e sera aplicado o desconto correspondente se houver.
if quantidade <= 9:
    desconto = 0  # O desconto será definido como 0% para quantidades até 9
elif quantidade <= 99:
    desconto = 5  # O desconto será definido com                       o 5% para quantidades entre 10 e 99
else:
    desconto = 10  # O desconto será definido como 10% para quantidades acima de 99


# Calculando o valor total com desconto
total_com_desconto = subtotal * (1 - desconto / 100)  # Calcula o valor total com desconto


# Exibindo o subtotal e o total com desconto
print("O valor total sem desconto é: R$ {:.2f}".format(subtotal))  # Exibe o subtotal sem desconto formatado com duas casas decimais convertendo para Real (R$)
print("O valor total com desconto é: R$ {:.2f}".format(total_com_desconto))  # Exibe o total com desconto formatado com duas casas decimais convertendo para Real (R$)


# Verificando se houve desconto
if desconto > 0:
    print("Foi aplicado um desconto de {}%.".format(desconto))  # Exibe a mensagem de desconto aplicado
else:
    print("Não foi aplicado nenhum desconto.")  # Exibe a mensagem de ausência de desconto


print("Obrigado pela preferência, volte sempre!!") # Exibe mensagem de agradecimento
