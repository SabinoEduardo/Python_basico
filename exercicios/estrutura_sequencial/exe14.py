#!    Leia a teoria para entender o código...
#? João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

from tkinter import *
from tkinter import ttk

#! Terminar de resolver este exercício, seu vagabundo...

class My_Class():
    def __init__(self):

        # Criando um objeto tkinter, definindo a geometria e o título.

        self.root = Tk()
        self.root.title("Salário por horas trabalhadas")
        self.root.geometry("350x180+25+25")
        self.root.resizable(0, 1)

        # Frame
        self.minha_frame = ttk.Frame(self.root, padding=(25, 20, 45, 10))

        #Variaveis
        self.var1_ganho_hora = StringVar()  # Ganho por horas
        self.var2_hora_trabalho = StringVar() # Horas trabalhadas no mês
        self.var3_salario_mes = StringVar() # Salário no mês

        #Widgets
        self.label_ganho_hora = ttk.Label(self.minha_frame, text="Salário por hora (R$):")
        self.entrada_ganho_hora = ttk.Entry(self.minha_frame, textvariable=self.var1_ganho_hora, width=25,)

        self.label_hora_trabalho = ttk.Label(self.minha_frame, text="Horas trabalhas no mês:")
        self.entrada_hora_trabalho = ttk.Entry(self.minha_frame, textvariable=self.var2_hora_trabalho, width=25)

        self.label_salario_mes = ttk.Label(self.minha_frame, text="Salário por mês (R$):")
        self.saida_salario_mes = ttk.Label(self.minha_frame, textvariable=self.var3_salario_mes, 
                                            background="#ccccb3", font="Arial 10 bold", width=22, anchor="center")

        self.btn = ttk.Button(self.root, text="Calcular", command=self.area, padding=5)
        self.label_erro = Label(self.root, text=" ", fg="red", font="Arial 10 bold")

        #Layout
        self.minha_frame.grid(row=0, column=0) 
        

        self.label_ganho_hora.grid(row=0, column=0)
        self.entrada_ganho_hora.grid(row=0, column=1)

        self.label_hora_trabalho.grid(row=1, column=0, pady=8)
        self.entrada_hora_trabalho.grid(row=1, column=1)

        self.label_salario_mes.grid(row=2, column=0)
        self.saida_salario_mes.grid(row=2, column=1)

        self.btn.grid(columnspan=2, padx=30, pady=10)
        self.label_erro.grid(pady=10)

        self.entrada_ganho_hora.focus()


        self.root.mainloop() # Metodo mainloop

    def area(self):
        """
            Função para calcular o valor da área de um círculo 
        """
        try:
            self.root.geometry("350x180")
            self.ganho_hora = float(self.var1_ganho_hora.get())
            self.hora_mes = float(self.var2_hora_trabalho.get())
            self.var3_salario_mes.set(round((self.ganho_hora*self.hora_mes), 2))
            self.label_erro["text"] = " "
        
        except:
            self.root.geometry("350x250")
            self.label_erro["text"] = "Erro!\nVerifique os valores digitados e tente novamente."
            self.var3_salario_mes.set(" ")
           


salario = My_Class() # Criando um objeto da classe Area_circulo