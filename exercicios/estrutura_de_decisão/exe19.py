#
#? Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
#* Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo: 326 = 3 centenas, 2 dezenas e 6 unidades 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

print("-"*80)
print("          Esse número analisa números inteiros menores que 1000")
print("-"*80)
n = int(input("Digite um número:"))
if n < 1000 and n > 0:
    print(f"O número {n} possui:")
    if n >= 100:
        centena = n//100
        n %= 100
        dezena = n//10
        n %= 10
        unidade = n
        print(f"{centena} centena(s)\n{dezena} dezena(s)\n{unidade} unidade(s)")
    elif n >= 10:
        centena = 0
        dezena = n//10
        n %= 10
        unidade = n
        print(f"{dezena} dezena(s)\n{unidade} unidade(s)")
    else:
        centena = 0
        dezena = 0
        unidade = n
        print(f"{unidade} unidade(s)")
else:
    print("Número inválido")
