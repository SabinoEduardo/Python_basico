from random import randint

while True:
    cpf = ""
    for i in range(11):
        cpf += str(randint(0, 9))

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
    if cpf == novo_cpf:
        break

print(cpf)