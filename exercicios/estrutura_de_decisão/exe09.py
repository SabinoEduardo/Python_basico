#
#? Faça um Programa que leia três números e mostre-os em ordem decrescente.

#! Esse problema será resolvido sem o módulo tkinter

def ordem_decrescente(n1, n2, n3):
    maior = menor  = medio = n1

    #* maior número
    if n2 > maior:
        maior = n2
    elif n3 > maior:
        maior = n3

    #* menor número
    if n2 < menor:
        menor = n2
    elif n3 < menor:
        menor = n3

    #* médio número
    if menor < n2 < maior:
        medio = n2
    elif menor < n3 < maior: 
        medio = n3

    return maior, medio, menor

n1 = float(input("N1:"))
n2 = float(input("N2:"))
n3 = float(input("N3:"))
print(ordem_decrescente(n1, n2, n3))
