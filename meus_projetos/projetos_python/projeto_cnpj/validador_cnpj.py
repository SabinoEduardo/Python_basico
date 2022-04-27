from minhas_funcoes import validar_cnpj

cnpj = "57570945341900"   # Variavel de entrada de cnpj

if validar_cnpj(cnpj):  # Saída do resultado
    print(f"{cnpj} CNPJ Válido")
else:
    print(f"{cnpj} CNPJ Inválido")
