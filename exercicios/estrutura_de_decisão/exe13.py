#
#? Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

def dia_semana(n):
    if n == 1:
        dia = "Domingo"
    elif n == 2:
        dia = "Segunda"
    elif n == 3:
        dia = "Terça"
    elif n == 4:
        dia = "Quarta"
    elif n == 5:
        dia = "Quinta"
    elif n == 6:
        dia = "Sexta"
    elif n == 7:
        dia = "Sabado"
    else:
        dia = "Inválido"

    return dia

numero = int(input("Digite um número:"))
print(f"O dia correspondente ao número {numero} é: {dia_semana(numero)}")
