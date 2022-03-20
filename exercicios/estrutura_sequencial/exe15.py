# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

#*  Salário bruto.
#*  Quanto pagou ao INSS.
#*  Quanto pagou ao sindicato.
#*  o salário líquido.

#TODOS Calcule os descontos e o salário líquido, conforme a tabela abaixo:
#* + Salário Bruto : R$
#* - IR (11%) : R$
#* - INSS (8%) : R$
#* - Sindicato ( 5%) : R$
#* = Salário Liquido : R$

from tkinter import *
from tkinter import ttk


class Area_circulo():
    def __init__(self):

        # Criando um objeto tkinter, definindo a geometria e o título.

        self.root = Tk()
        self.root.title("Salário Líquido Mensal")
        self.root.geometry("350x180+25+25")
        self.root.resizable(1, 1)

        # Frame
        self.minha_frame = ttk.Frame(self.root, padding=(25, 20, 45, 10))

        #Variaveis
        self.var1_ganho_hora = StringVar()  # Ganho por horas
        self.var2_hora_trabalho = StringVar() # Horas trabalhadas no mês
        self.var3_salario_mes = StringVar() # Salário no mês

        #Widgets
        self.label_ganho_hora = ttk.Label(self.minha_frame, text="Salário por hora (R$):")
        self.entrada_ganho_hora = ttk.Entry(self.minha_frame, textvariable=self.var1_ganho_hora, width=25,
                                                justify="center")

        self.label_hora_trabalho = ttk.Label(self.minha_frame, text="Horas trabalhas no mês:")
        self.entrada_hora_trabalho = ttk.Entry(self.minha_frame, textvariable=self.var2_hora_trabalho, 
                                                justify="center", width=25)

        self.label_salario_mes = ttk.Label(self.minha_frame, text="Salário por mês (R$):")
        self.saida_salario_mes = ttk.Label(self.minha_frame, textvariable=self.var3_salario_mes, 
                                            background="#ccccb3", font="Arial 10 bold", width=22, anchor="center")

        self.btn = ttk.Button(self.root, text="Calcular Salário", command=self.area, padding=5)
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
            salario_bruto = float(self.var2_hora_trabalho.get()) * float(self.var1_ganho_hora.get()) 
            valor_IR = salario_bruto * 11 / 100
            valor_INSS = salario_bruto * 8 / 100
            sindicato = salario_bruto * 5 / 100
            self.var3_salario_mes.set(round((salario_bruto - valor_IR - valor_INSS - sindicato), 2))
        except:
            self.var3_salario_mes.set("Erro!\nVerifique o valor digitado")
            self.saida_salario_mes["width"] = 23
            self.saida_salario_mes["foreground"] = "Red"
            self.saida_salario_mes["justify"] = "center"
            self.saida_salario_mes["font"] = "Arial 9 bold"
           

salario = Area_circulo() # Criando um objeto da classe Area_circulo