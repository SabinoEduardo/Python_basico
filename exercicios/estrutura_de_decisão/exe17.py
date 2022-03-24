#
#? Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

def ano_bissexto(ano):
    if (ano % 4 == 0 and ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
            msg = "é ano bissexto"
    else:
        msg = "não é bissexto"
    return msg

ano = int(input("Digite ano:"))
print(f"{ano} {ano_bissexto(ano)}")
