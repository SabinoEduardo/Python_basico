#
#? Faça um programa que leia 5 números e informe o maior número.

maior = float(input(f"Número {1}:"))
for i in range(1, 5):
    num = float(input(f"Número {i+1}:"))
    if num > maior:
        maior = num
print(maior)