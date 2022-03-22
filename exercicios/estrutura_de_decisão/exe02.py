#
#TODO - Neste exercício não será usado o módulo tkinter

#? Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

def positivo_negativo(n):
    if n > 0:
        return "positivo."
    elif n < 0:
        return "negativo."
    else:
        return "igual a zero."

n = float(input("Digite um número:"))
print(f"O número digitado é {positivo_negativo(n)}")