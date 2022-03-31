#
# ? Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
# pedindo até que o usuário informe um valor válido.

while True:
    print("Digite uma nota entre 0 a 10.")
    nota = float(input("Nota:"))
    if 0 <= nota <= 10:
        print("Correct")
        break
    else:
        print("Value invalid")
