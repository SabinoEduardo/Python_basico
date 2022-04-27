cpf = input("Digite seu CPF:")
caracteres = ".-"

for i in range(len(caracteres)):
    cpf = cpf.replace(caracteres[i], "")

novo_cpf = cpf[:9]
count = 10
while count <= 11:
    soma = 0
    for index, value in enumerate(novo_cpf):
        mult = int(count - index) * int(value)
        soma += mult

    if (soma % 11) < 2:
        digito = 0
    else:
        digito = 11 - (soma % 11)

    novo_cpf += str(digito)
    count += 1

sequencia = novo_cpf == str(novo_cpf[0]) * 11
if cpf == novo_cpf and not sequencia:
    print("sdaCPF Válido!")
else:
    print("CPF Inválido!")
