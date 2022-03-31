#
#? Faça um programa que calcule o mostre a média aritmética de N notas.

soma_notas, qtde_nota =0, int(input("Quantidade de notas:"))
for i in range(1, qtde_nota + 1):
    nota = float(input(f"Nota{i}: "))
    soma_notas += nota

media_nota = soma_notas/qtde_nota
print(f'{"Média de ":>30}{qtde_nota} notas')
print(f"Média = {media_nota}")