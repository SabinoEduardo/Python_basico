#
#? Altere o programa de cálculo do fatorial (exe17.py), permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

print(f'{"Fatorial":>25}')

while True:
    res, num = 1, int(input("Digite um número:"))
    if 0 <= num < 16:
        print(f"{num}! = ", end="")
        while num >= 1:
            if num != 0:
                res *= num
                print(f"{num} X ", end="") if num > 1 else print(f"{num} =", end=" ")
                num -= 1
        print(res)
    else:
        if num < 0:
            print("Não existe factorial de número negativo")
        else:
            print("O número deve ser positivo e menor que 16")
        


