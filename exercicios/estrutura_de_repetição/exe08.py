#
#? Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = count = 0
while count < 5:
    num = float(input(f"Número {count + 1}:"))
    soma += num
    count += 1

print(f"Soma = {soma:.2f}")
print(f"Média = {soma/count:.2f}")