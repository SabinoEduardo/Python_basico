#  
    # * param Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre 
    # * o produto do dobro do primeiro com metade do segundo .
    # * a soma do triplo do primeiro com o terceiro.
    # * o terceiro elevado ao cubo.

    #! Neste exercício não usarei o modulo tkinter.
    #? Não foi aplicado nenhuma condição e nem excessão de erro

def calculos():
    n1_int = int(input("Número 1 (Inteiro):"))
    n2_int = int(input("Número 2 (Inteiro):"))
    n3_float = float(input("Número 1 (Real):"))
    res_1 = round((2*n1_int)*(n2_int/2), 2)
    res_2 = round((3*n1_int + n3_float), 2)
    res_3 = round(n3_float**3, 2)
    return res_1, res_2, res_3

res = calculos()
print(res)
