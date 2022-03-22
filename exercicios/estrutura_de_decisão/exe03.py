#
#TODO - Neste exercício não será usado o módulo tkinter

#? Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

def check_sexo(sexo):
    if sexo == "M":
        return "Masculino"
    elif sexo == "F":
        return "Feminino"
    else:
        return "Invalido"

sexo = str(input("Digite o sexo[M/F]:")).upper()
print(f"Sexo {check_sexo(sexo)}")