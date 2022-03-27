#
#? Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#* par ou ímpar;
#* positivo ou negativo;
#* inteiro ou decimal.


from math import ceil

class My_Class():
    def __init__(self):
        self.n1 = float(input("Primeiro Número:"))
        self.n2 = float(input("Segundo Número:"))
       

    def soma(self, n1, n2):
        self.resultado = n1 + n2
        return self.resultado, self.par_impar(self.resultado), self.negativo_positivo(self.resultado), self.inteiro_decimal(self.resultado)

    def subtracao(self, n1, n2):
        self.resultado = n1 - n2
        return self.resultado, self.par_impar(self.resultado), self.negativo_positivo(self.resultado), self.inteiro_decimal(self.resultado)

    def multiplicação(self, n1, n2):
        self.resultado = n1 * n2
        return self.resultado, self.par_impar(self.resultado), self.negativo_positivo(self.resultado), self.inteiro_decimal(self.resultado)

    def divisao(self, n1, n2):
        self.resuldato = n1 / n2
        return self.resultado, self.par_impar(self.resultado), self.negativo_positivo(self.resultado), self.inteiro_decimal(self.resultado)

    def par_impar(self, resultado):
        if resultado % 2 == 0:
            return "par"
        else:
            return "impar"

    def negativo_positivo(self, resultado):
        if resultado > 0:
            return "Positivo"
        else:
            return "Negativo"

    def inteiro_decimal(self, resultado):
        if resultado == ceil(resultado):
            return "Inteiro"
        else:
            return "Decimal"
    
    
calculador = My_Class()
option = int(input("Qual o número da operação desejas realizar?\n[1] - Soma\n[2] - Subtração\n[3] - Multiplicação\n[4] - Divisão\nR:"))
        
if option == 1:
    print(calculador.soma(calculador.n1, calculador.n2))
elif option == 2:
     print(calculador.subtracao(calculador.n1, calculador.n2))
elif option == 3:
     print(calculador.multiplicação(calculador.n1, calculador.n2))
elif option == 4:
     print(calculador.divisao(calculador.n1, calculador.n2))
else: 
    print("Opção errada")
