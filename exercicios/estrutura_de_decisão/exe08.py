#
#? Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

def menor_preco(p1, p2, p3):
    #* Menor número
    menor = p1
    if p2 < menor:
        menor = p2
    elif p3 < menor:
        menor = p3
    return menor


preco1 = float(input("Preço do produto1:"))
preco2 = float(input("Preço do produto2:"))
preco3 = float(input("Preço do produto3:"))
print(f"O menor preço é: {menor_preco(preco1, preco2, preco3)}")
