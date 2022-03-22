#
#TODO - Neste exercício não será usado o módulo tkinter

#? Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

def check_letra(letra):
    letras_consoante = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z")

    letras_vogal = ("a", "e", "i", "o", "u", "y")

    if letra in letras_consoante:
            return "Consoante"
    elif letra in letras_vogal:
            return "Vogal"
    else:
        return "Não é letra"

letra = str(input("Digite uma letra:"))
print(check_letra(letra))