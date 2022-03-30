#
#? Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

print(f'{"Fatorial":>25}')

res, num = 1, int(input("Digite um número:"))
if num >= 0:
    print(f"{num}! = ", end="")
    while num >= 1:
        if num != 0:
            res *= num
            print(f"{num} X ", end="") if num > 1 else print(f"{num} =", end=" ")
            num -= 1
    print(res)
else:
    print("Não existe factorial de número negativo")

