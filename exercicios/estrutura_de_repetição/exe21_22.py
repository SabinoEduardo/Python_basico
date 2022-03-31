#
#? Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

count = 0
num = int(input("Digite um número inteiro:"))
print(f"O número {num} é divisivel por: ", end="")
for i in range(1, num+1):
    if num % i == 0:
        count += 1
        print(i, end=", ") if i < num else print(i)
if count == 2:
    print(f"{num} é número primo")
else:
    print(f"{num} não é numero primo")
    