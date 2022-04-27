import re
from random import randint


REGRESSIVA = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def remover_caracter(cnpj):
    cnpj = re.sub(r"[^0-9]", "", cnpj)
    return cnpj


def formata_cnpj(cnpj):
    cnpj = f"{cnpj[0:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}"
    return cnpj


def eh_sequencia(cnpj):
    sequencia = cnpj[0] * len(cnpj)
    if sequencia == cnpj:
        return True


def validar_cnpj(cnpj, codigo):
    cnpj = remover_caracter(cnpj)
    cnpj_novo = cnpj[:-2]
    for i in range(1, -1, -1):
        soma = 0
        for indice, value in enumerate(cnpj_novo):
            soma += REGRESSIVA[indice + i] * int(value)
        digito = 11 - (soma % 11)
        cnpj_novo += str(digito) if digito <= 9 else "0"
    if eh_sequencia(cnpj):
        return False
    else:
        if codigo == 0:
            if cnpj == cnpj_novo:
                return cnpj_novo
        else:
            return cnpj_novo


def gera_cnpj():
    primeiro_digito = randint(0, 9)
    segundo_digito = randint(0, 9)
    segundo_bloco = randint(100, 999)
    terceito_bloco = randint(100, 999)
    quarto_bloco = "0001"
    cnpj_incio = f"{primeiro_digito}{segundo_digito}{segundo_bloco}{terceito_bloco}{quarto_bloco}00"
    return formata_cnpj(validar_cnpj(cnpj_incio, 1))
