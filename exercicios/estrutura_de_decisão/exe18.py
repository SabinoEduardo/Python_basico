#
#? Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.


def validacao_data(dia, mes, ano):

    try:
        if len(ano) == 4 and dia > 0:
            if mes == "02":
                if (int(ano) % 4 == 0 and int(ano) % 100 != 0) or (int(ano) % 4 == 0 and int(ano) % 400 == 0):
                    if dia <= 29:
                        value_dia = dia
                        value_mes = mes

                else: 
                    if dia <= 28:
                        value_dia = dia
                        value_mes = mes
                    
                    
            if mes in ("1", "3", "5", "7", "8", "10","12") and dia in ("1", "2", "3", "4", "5", "6", "7", "8","9","'10", "11",  "12", "13", "14", "15", "16", "17", "18", "19","'20", "21", "22", "23", "24", "25", "26", "27", "28", "29","'30", "31"):
                value_dia = dia
                value_mes = mes

            elif mes in ("4", "6", "9", "11") and dia in ("1", "2", "3", "4", "5", "6", "7", "8", "9","'10", "11", "12", "13", "14", "15", "16", "17", "18", "19","'20","21", "22", "23", "24", "25", "26", "27", "28", "29","'30"):
                value_dia = dia
                value_mes = mes
        return f"{value_dia}/{value_mes}/{ano}\nData válida"

    except:
        return "Data inválida"


print("\nValidaçao de data no formato dd/mm/aaaa")
print("-"*60)
dia = str(input("Dia:"))
mes = str(input("Mês:"))
ano = str(input("Ano:"))
print("-"*60)
print(validacao_data(dia, mes, ano))
                    