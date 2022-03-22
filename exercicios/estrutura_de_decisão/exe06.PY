#
#? Faça um Programa que leia três números e mostre o maior e o menor deles.

#TODO - Aqui foi resolvido o exercício 6 e 7

#! Esse problema será resolvido sem o módulo tkinter

def maior_numero(n1, n2, n3):
    #* Maior número
    maior = n1
    if n2 > maior:
        maior = n2
    elif n3 > maior:
        maior = n3
    return maior

def menor_numero(n1, n2, n3):
    #* Menor número
    menor = n1
    if n2 < menor:
        menor = n2
    elif n3 < menor:
        menor = n3
    return menor

n1 = float(input("N1:"))
n2 = float(input("N2:"))
n3 = float(input("N3:"))
print(f"O maior número é: {maior_numero(n1, n2, n3)}")
print(f"O menor número é: {menor_numero(n1, n2, n3)}")
