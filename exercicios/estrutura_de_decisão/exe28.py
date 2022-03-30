#
#? O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#*                     Até 5 Kg            Acima de 5 Kg
#* File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#* Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#* Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

#? Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

print("-"*80)
print(f'{"Até 5 Kg ": >35}{"Acima de 5 Kg": >30}')
print(f'{"[1] - File Duplo": <23}{"R$ 4,90 por Kg": <18}{"R$ 5,80 por Kg": >25}')
print(f'{"[2] - Alcatra": <23}{"R$ 5,90 por Kg": <18}{"R$ 6,80 por Kg": >25}')
print(f'{"[3] - Picanha": <23}{"R$ 6,90 por Kg": <18}{"R$ 7,80 por Kg": >25}')
print("-"*80)

option = int(input("Choice the type of meat:"))
if option in (1, 2, 3):
    the_amount = float(input("How many kilos?\nAnswer:"))
    if option == 1:
        if the_amount <= 5:
            price = the_amount*4.90
        else:
            price = the_amount*5.80
    elif option == 2:
        if the_amount <= 5:
            price = the_amount*5.90
        else:
            price = the_amount*6.80
    else:
        if the_amount <= 5:
            price = the_amount*6.90
        else:
            price = the_amount*7.80

    print("-"*80)
    print(f'{"Pay Metod":>30}')
    print("[1] - Tabajara Card")
    print("[2] - Others")

    pay_metod = int(input("What is the pay metod?\nAnswer:"))
    if pay_metod == 1:
        price -= price*0.05

    print("-"*80)
    print(f"The amount of meat: {the_amount:.2f} Kg")
    print(f"Price to pay: R${price:.2f}")

else:
    print("Error type of meat")


