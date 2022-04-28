from minhas_funcoes import valida_cnpj, remover_caracter

cnpj = "71.312.700/0001-60"   # Variavel de entrada de cnpj
if remover_caracter(cnpj) == valida_cnpj(cnpj, 0):
    print(f"{cnpj} CNPJ Válido")
else:
    print(f"{cnpj} CNPJ Inválido")
