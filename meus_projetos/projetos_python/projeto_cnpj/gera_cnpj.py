from random import randint
from minhas_funcoes import validar_cnpj

while True:
    cnpj = randint(10000000000000, 99999999999999)
    if validar_cnpj(str(cnpj)):  # Saída do resultado
        print(f"CNPJ gerado: {cnpj}")
        break
