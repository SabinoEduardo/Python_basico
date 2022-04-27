from random import randint
from minhas_funcoes import valida_cpf


while True:
    cpf = str(randint(10000000000, 99999999999))
    if valida_cpf(cpf):
        print(f"CPF gerado: {cpf}")
        break
