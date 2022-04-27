import re


REGRESIVA = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]


def remove_caractere(cpf):
    cpf = re.sub(r"[^0-9]", "", cpf)
    return cpf


def novo_cpf(cpf):
    cpf = cpf[:-2]
    for i in range(1, -1, -1):
        soma = 0
        for index, value in enumerate(cpf):
            soma += REGRESIVA[index + i] * int(value)
        resto = soma % 11
        cpf += "0" if resto < 2 else str(11 - resto)
    return cpf


def is_senquence(cpf):
    seuqencia = cpf[0] * len(cpf)
    if cpf == seuqencia:
        return True


def valida_cpf(cpf):
    cpf = remove_caractere(cpf)
    if is_senquence(cpf):
        return False
    cpf1 = novo_cpf(cpf)
    if cpf == cpf1:
        return True
    else:
        return False
