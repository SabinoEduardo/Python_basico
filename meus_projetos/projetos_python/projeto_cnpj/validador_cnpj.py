from minhas_funcoes import validar_cnpj, remover_caracter

cnpj = "37.328.917/0001-20"   # Variavel de entrada de cnpj

if remover_caracter(cnpj) == validar_cnpj(cnpj, 0):
    print(f"{cnpj} CNPJ Válido")
else:
    print(f"{cnpj} CNPJ Inválido")
