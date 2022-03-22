#
#TODO - Neste exercício não será usado o módulo tkinter

#? Faça um Programa que peça dois números e imprima o maior deles.

def maiorNumero(n1, n2):
    if n1 > n2:
        return f"O maior número é {n1}"
    elif n1 < n2:
         return f"O maior número é {n2}"
    else:
        return "Os números são iguais"

n1 = float(input("Número 1:"))
n2 = float(input("Número 2:"))
print(maiorNumero(n1, n2))