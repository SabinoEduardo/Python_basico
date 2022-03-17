# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

from tkinter import *
from tkinter import ttk


class Area_circulo():
    def __init__(self):

        # Criando um objeto tkinter, definindo a geometria e o título.

        self.root = Tk()
        self.root.title("Salário por horas trabalhadas")
        self.root.geometry("350x180")
        self.root.resizable(0, 1)

        # Frame
        self.minha_frame = ttk.Frame(self.root, padding=(28, 20, 45, 10))

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
                                            background="#ccccb3", width=25)

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
            self.root.geometry("350x150")
            self.ganho_hora = float(self.var1_ganho_hora.get())
            self.hora_mes = float(self.var2_hora_trabalho.get())
            self.var3_salario_mes.set(round((self.ganho_hora*self.hora_mes), 2))
            self.label_erro["text"] = " "
        
        except:
            self.root.geometry("350x250")
            self.label_erro["text"] = "Erro!\nVerifique os valores digitados e tente novamente."
            self.var3_salario_mes.set(" ")
           


salario = Area_circulo() # Criando um objeto da classe Area_circulo