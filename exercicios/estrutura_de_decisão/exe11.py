#
#?As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#?Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#* salários até R$ 280,00 (incluindo) : aumento de 20%
#* salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#* salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#* salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#TODO a) O salário antes do reajuste;
#TODO b) O percentual de aumento aplicado;
#TODO c) O valor do aumento;
#TODO d) O novo salário, após o aumento.

#! Será usado o módulo Tkinter para a resolção deste problema

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class My_Class():
    def __init__(self):

        #* Criate tkinter object and my_frame.
        self.parent = Tk()
        self.parent.title("Organizações Tabajara")
        self.parent.geometry("400x240+30+30")
        self.my_frame = ttk.Frame(self.parent, border=2, relief=SOLID, padding=(10))

        #* My variables
        self.salario_atual = StringVar()
        self.taxa = StringVar()
        self.aumento = StringVar()
        self.salario_novo = StringVar()

        #* Create my widgets
        self.text_salario_atual = ttk.Label(self.my_frame, text="Salário Atual:", font="Arial 10 bold")
        self.input_salario_atual = ttk.Entry(self.my_frame, textvariable=self.salario_atual, width=25, justify="center")

        self.text_taxa_reajuste = ttk.Label(self.my_frame, text="Taxa de reajuste:", font="Arial 10 bold")
        self.output_taxa_reajuste = ttk.Label(self.my_frame, textvariable=self.taxa, width=22, justify="center",
                                       anchor="center", background="#ccccb3", font="Arial 10 bold")

        self.text_aumento = ttk.Label(self.my_frame, text="Valor do aumento:", font="Arial 10 bold")
        self.output_aumento = ttk.Label(self.my_frame, textvariable=self.aumento, background="#ccccb3", 
                                        width=22, anchor="center", justify="center", font="Arial 10 bold")

        self.text_salario_novo = ttk.Label(self.my_frame, text="Novo Salário:", 
                                        font="Arial 10 bold")

        self.output_salario_novo = ttk.Label(self.my_frame, textvariable=self.salario_novo, background="#ccccb3",
                                        width=22, anchor="center", justify="center", 
                                        font="Arial 10 bold")

        self.btn = Button(self.parent, text="Calcular Média", width=15, background="#ff6666",
                            font="Arial 12 bold", command=self.media_situacao)

        self.my_frame.grid(row=0, column=0, padx=45, pady=20)

        self.text_salario_atual.grid(row=0, column=0)
        self.input_salario_atual.grid(row=0, column=1)

        self.text_taxa_reajuste.grid(row=1, column=0, pady=10)
        self.output_taxa_reajuste.grid(row=1, column=1)

        self.text_aumento.grid(row=2, column=0)
        self.output_aumento.grid(row=2, column=1)

        self.text_salario_novo.grid(row=3, column=0)
        self.output_salario_novo.grid(row=3, column=1, padx=3, pady=10)

        self.btn.grid(row=1)

        self.input_salario_atual.focus()

        self.parent.mainloop()

    def media_situacao(self):
       
        try:
            salario_atual = float(self.salario_atual.get())
            if salario_atual <= 280:
                self.taxa.set("20%")
                self.aumento.set(salario_atual*0.20)
                self.salario_novo.set(salario_atual + salario_atual*0.20)
            elif salario_atual <= 700:
                self.taxa.set("15%")
                self.aumento.set(salario_atual*0.15)
                self.salario_novo.set(salario_atual + salario_atual*0.15)
            elif salario_atual <= 1500:
                self.taxa.set("10%")
                self.aumento.set(salario_atual*0.10)
                self.salario_novo.set(salario_atual + salario_atual*0.10)
            else:
                self.taxa.set("5%")
                self.aumento.set(salario_atual*0.05)
                self.salario_novo.set(salario_atual + salario_atual*0.5)
        except:
            messagebox.showerror("Mensagem de erro", "Verifique o valor salário.")
         
notas_situação = My_Class()
