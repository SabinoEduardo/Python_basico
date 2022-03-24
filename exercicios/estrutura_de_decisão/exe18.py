#
#? Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

dia = str(input("Dia"))
mes = str(input("Mês:"))
ano = str(input("Ano:"))
lista_dias = ["01", "02", "03", "04", "05", "06", "07", "08", "09","'10",
                "11", "12", "13", "14", "15", "16", "17", "18", "19","'20",
                "21", "22", "23", "24", "25", "26", "27", "28", "29","'30", "31"]

lista_meses = ["01", "02", "03", "04", "05", "06", "07", "08", "09","'10",
                "11", "12"]

if dia in lista_dias:
    if mes in lista_meses:
        if mes == "02"