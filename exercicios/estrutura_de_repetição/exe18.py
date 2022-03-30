#
#? Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

soma , qtde_num = 0, int(input("Digite a quantidade de números:"))
for i in range(1, qtde_num + 1):
    num = float(input(f"Número {i}: "))
    soma += num
    if i == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        else:
            if num < menor:
                menor = num
print("-"*45)
print(f"Maior = {maior}")
print(f"Menor = {menor}")
print(f"Soma = {soma}")
