#
#? Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa #? deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

num = int(input("Digite um número inteiro:"))
count = qtde_divisao = 0

print(f"Número primos entre 1 e {num}: ")
for n in range(2, num):
    for i in range(1, n+1):
        if n % i == 0:
            count += 1

    if count == 2:
        print(n)
        qtde_divisao += count
    count = 0
print(f"Foram executadas {qtde_divisao} divisões para encontrar os números primos.")
