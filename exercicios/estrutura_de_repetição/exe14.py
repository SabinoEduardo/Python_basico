#
#? Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

qtde_par = qtde_impar = 0

for i in range(1, 11):
    numero = int(input(f"Número {i}: "))
    if numero % 2 == 0:
        qtde_par += 1
    else:
        qtde_impar += 1
print(f"Quantidade de números pares: {qtde_par}")
print(f"Quantidade de números impares: {qtde_impar}")