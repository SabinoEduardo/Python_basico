#
#?Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

#* Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#* Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.


nota = int(input("Valor do saque:"))
if 10 <= nota <= 600:
    if nota >= 100:
        nota_100 = nota//100
        print(f"{nota_100} notas de 100")
        nota %= 100
    if nota >= 50:
        nota_50 = nota//50
        print(f"{nota_50} notas de 50")
        nota %= 50
    if nota >= 10:
        nota_10 = nota//10
        print(f"{nota_10} notas de 10")
        nota %= 10
    if nota >= 5:
        nota_5 = nota//5
        print(f"{nota_5} notas de 5")
    if nota >= 1:
        nota_1 = nota
        print(f"{nota_1} notas de 1")
else:
    print("Valor não liberado para saque")