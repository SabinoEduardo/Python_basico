#!    Leia a teoria para entender o código...
#? João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

from tkinter import *
from tkinter import ttk


class My_Class():
    def __init__(self):

        # Criando um objeto tkinter, definindo a geometria e o título.

        self.root = Tk()
        self.root.title("Dados da pesca")
        self.root.geometry("400x220+25+25")
        self.root.resizable(0, 0)

        # Frame
        self.minha_frame = ttk.Frame(self.root, padding=(15, 20), border=1, relief=SOLID)

        #Variaveis
        self.var1_peso_total = StringVar()  # peso total do peixes
        self.var2_peso_excesso = StringVar() # Horas trabalhadas no mês
        self.var3_multa = StringVar() # Salário no mês

        #Widgets
        self.text_peso = ttk.Label(self.minha_frame, text="Peso total(kg):")
        self.entrada_peso = ttk.Entry(self.minha_frame, textvariable=self.var1_peso_total, 
                                        width=25, justify="center")

        self.text_excesso = ttk.Label(self.minha_frame, text="Peso em excesso(kg):")
        self.saida_peso_excesso = ttk.Label(self.minha_frame, textvariable=self.var2_peso_excesso, 
                                                width=20, background="#ccccb3", anchor="center", 
                                                justify="center", font="Arial 11 bold")

        self.text_multa = ttk.Label(self.minha_frame, text="Valor da Multa(R$):")
        self.saida_multa = ttk.Label(self.minha_frame, textvariable=self.var3_multa, 
                                            background="#ccccb3", font="Arial 11 bold", 
                                            width=20, anchor="center", foreground="red")

        self.btn = Button(self.root, text="Calcular Multa", command=self.area, background="#ff6666",
                            font="Arial 12 bold"    )

        #Layout
        self.minha_frame.grid(row=0, column=0, padx=50, pady=15) 
        
        self.text_peso.grid(row=0, column=0)
        self.entrada_peso.grid(row=0, column=1)

        self.text_excesso.grid(row=1, column=0, pady=8)
        self.saida_peso_excesso.grid(row=1, column=1)

        self.text_multa.grid(row=2, column=0)
        self.saida_multa.grid(row=2, column=1)

        self.btn.grid(columnspan=2, padx=30, pady=5)

        self.entrada_peso.focus()

        self.root.mainloop() # Metodo mainloop

    def area(self):
        """
            Função para calcular o valor da área de um círculo 
        """
        try:
            peso = float(self.var1_peso_total.get())
            excesso_peso = peso - 50
            multa = excesso_peso*4
            self.var2_peso_excesso.set(round(excesso_peso, 2))
            self.var3_multa.set(multa*4)
        except:
            self.var3_multa.set("Erro!\nVerifique o valor digitado")
            self.saida_multa["width"] = 23
            self.saida_multa["foreground"] = "Red"
            self.saida_multa["justify"] = "center"
            self.saida_multa["font"] = "Arial 9 bold"
           


salario = My_Class() # Criando um objeto da classe Area_circulo