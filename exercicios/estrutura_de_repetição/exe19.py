#
#? Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

soma , qtde_num = 0, int(input("Digite a quantidade de números:"))
i = 1
while qtde_num >= i:
#for i in range(1, qtde_num + 1):
    num = float(input(f"Número {i}: "))
    if num > 0 and num < 100:
        soma += num
        if  i == 1:
            maior = menor = num
        else:
            if num > maior:
                maior = num
            else:
                if num < menor:
                    menor = num
        i += 1
    else:
        print("O sistema só aceita números entre 0 e 100")

print("-"*45)
print(f"Maior = {maior}")
print(f"Menor = {menor}")
print(f"Soma = {soma}")
