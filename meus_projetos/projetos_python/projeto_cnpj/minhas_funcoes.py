import re

REGRESSIVA = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def remover_caracter(cnpj):
    cnpj = re.sub(r"[^0-9]", "", cnpj)
    return cnpj


def novo_cnpj(cnpj):
    cnpj = cnpj[:-2]
     for i in range(1, -1, -1):
        soma = 0
        for indice, value in enumerate(cnpj):
            soma += REGRESSIVA[indice + i] * int(value)
        digito = 11 - (soma % 11)
        cnpj += str(digito) if digito <= 9 else "0"
    return cnpj


def eh_sequencia(cnpj):
    sequencia = cnpj[0] * len(cnpj)
    if sequencia == cnpj:
        return True


def validar_cnpj(cnpj):
    cnpj = remover_caracter(cnpj)
    if eh_sequencia(cnpj):
        return False
    else:
        cnpj1 = novo_cnpj(cnpj)
        if cnpj == cnpj1:
            return True
