#
#? Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

def par_impar(n):
    if n % 2 == 0:
        return "par"
    else:
        return "impar"
n = int(input("Digite um número interiro:"))

print(f"O número digitado é {par_impar(n)} ")
    