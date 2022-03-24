#
#? Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.


def validacao_data(dia, mes, ano):

    try:
        if len(ano) == 4:
            if mes == "02":
                if (int(ano) % 4 == 0 and int(ano) % 100 != 0) or (int(ano) % 4 == 0 and int(ano) % 400 == 0):
                    lista_dia = ("01", "02", "03", "04", "05", "06", "07", "08", "09","'10",
                                            "11", "12", "13", "14", "15", "16", "17", "18", "19","'20",
                                                "21", "22", "23", "24", "25", "26", "27", "28", "29")
                    

                else:  
                    lista_dia = ("01", "02", "03", "04", "05", "06", "07", "08", "09","'10",
                                            "11", "12", "13", "14", "15", "16", "17", "18", "19","'20",
                                                "21", "22", "23", "24", "25", "26", "27", "28")

                if dia in lista_dia:
                    value_dia = dia
                    value_mes = mes
                    
            if mes in ("01", "03", "05", "07", "08", "10","12") and dia in ("01", "02", "03", "04", "05", "06", "07", "08","09","'10", "11", "12",  "13", "14", "15", "16", "17", "18", "19","'20", "21", "22", "23", "24", "25", "26", "27", "28", "29","'30", "31"):
                value_dia = dia
                value_mes = mes

            elif mes in ("04", "06", "09", "11") and dia in ("01", "02", "03", "04", "05", "06", "07", "08", "09","'10", "11", "12", "13", "14", "15", "16", "17", "18", "19","'20","21", "22", "23", "24", "25", "26", "27", "28", "29","'30"):
                value_dia = dia
                value_mes = mes
        return f"{value_dia}/{value_mes}/{ano}\nData válida"

    except:
        return "Data inválida"


dia = str(input("Dia:"))
mes = str(input("Mês:"))
ano = str(input("Ano:"))
print("-"*45)
print(validacao_data(dia, mes, ano))
                    