from minhas_funcoes import valida_cpf


cpf = input("Digite seu CPF:")
if valida_cpf(cpf):
    print(f"CPF {cpf} é válido")
else:
    print(f"CPF {cpf} não é válido")
