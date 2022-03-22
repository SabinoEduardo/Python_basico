#
#? Faça um Programa que leia três números e mostre o maior e o menor deles.

#TODO - Aqui foi resolvido o exercício 6 e 7

#! Esse problema será resolvido sem o módulo tkinter

def maior_numero(n1, n2, n3):
    #* Maior número
   
    if n3 > n1 and n3 > n2:
        return n3
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n1

def menor_numero(n1, n2, n3):
    #* Menor número
   
    if n3 < n1 and n3 < n2:
        return n3
    elif n2 < n1 and n2 < n3:
        return n2
    else:
        return n1


n1 = float(input("N1:"))
n2 = float(input("N2:"))
n3 = float(input("N3:"))
print(f"O maior número é: {maior_numero(n1, n2, n3)}")
print(f"O menor número é: {menor_numero(n1, n2, n3)}")
