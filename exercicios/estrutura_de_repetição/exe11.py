#
#? Altere o programa anterior para mostrar no final a soma dos números.


n1 = int(input("Número 1:"))
n2= int(input("Número 2:"))
soma = 0
for n in range(n1+1, n2):
    print(n)
    soma += n
print(f"Soma dos números: {soma}")