#
#? Um posto está vendendo combustíveis com a seguinte tabela de descontos:

    #TODO - Álcool:
        #*  até 20 litros, desconto de 3% por litro
        #*  acima de 20 litros, desconto de 5% por litro
    #TODO - Gasolina:
        #* até 20 litros, desconto de 4% por litro
        #* acima de 20 litros, desconto de 6% por litro.

#? Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.


from tkinter import *
from tkinter import ttk

from click import option


class My_class():
    def __init__(self):

        # Criate parent object tk e as frames
        self.parent = Tk()
        self.parent.title("Preço total do combustivel")
        self.my_frame1 = ttk.Frame(self.parent, padding=(50, 5), width=40, border=1, relief=SOLID)
        self.my_frame2 = ttk.Frame(self.parent, padding=(30, 3), width=40)
        self.parent.geometry("380x230+50+35")
        self.parent.resizable(1, 0)
        

        # Variables
        self.option = IntVar()   
        self.qtde_litro = StringVar()
        self.preco_total = StringVar()  
        

        # Widgets

        self.text_radio = ttk.Label(self.my_frame1, text="Selecione uma opção", font="Arial 12 bold")
        self.gasolina = ttk.Radiobutton(self.my_frame1, text='Gasolina', variable=self.option, value=1)
        self.alcool = ttk.Radiobutton(self.my_frame1, text='Álcool', variable=self.option, value=0)

        self.text_entrada = ttk.Label(self.my_frame2, text="Quantidade de litros:", font="Arial 9 bold")
        self.qtde_litro_entry = ttk.Entry(self.my_frame2, justify="center", textvariable=self.qtde_litro)

        self.text_saida = ttk.Label(self.my_frame2, text="Preço Total:", font="Arial 9 bold")
        self.preco_total_exit = ttk.Label(self.my_frame2, background="#ccccb3", textvariable=self.preco_total, width=17, font="Arial 10 bold")

        self.buton = Button(self.parent, text="Preço Total", command=self.weigth_calculation, width=10, background="#ff3333", font="Arial 10 bold")


        # Layout
        self.my_frame1.grid(row=0, column=1, padx=55, pady=10)
        self.my_frame2.grid(row=1, column=1, padx=40)
        self.text_radio.grid()
        self.gasolina.grid()
        self.alcool.grid()
        
        self.text_entrada.grid(row=1, pady=5)
        self.qtde_litro_entry.grid(row=1, column=1)

        self.text_saida.grid(pady=8)
        self.preco_total_exit.grid(row=2, column=1)

        self.buton.grid(row=2, column=1)

        self.qtde_litro_entry.focus()
        
        self.parent.mainloop()
        

    def weigth_calculation(self):
        """
            Função para converter a temperatuda de uma unidade para outra.
        """
        
        try:
            if float(self.qtde_litro.get()) > 0:
                self.preco_total_exit["foreground"] = "black"
                self.preco_total_exit["font"] = "Arial 10 bold"
                self.preco_total_exit["anchor"] = "center"
                self.preco_total_exit["justify"] = "center"
                self.preco_total_exit["width"] = "17"
                litros = float(self.qtde_litro.get())
                if self.option.get() == 1:
                    if litros <= 20:
                        preco = litros*2.50 - litros*2.50*0.04    
                    else:
                        preco = litros*2.50 - litros*2.50*0.06
                else:   
                    if litros <= 20:
                        preco = litros*2.50 - litros*2.50*0.03    
                    else:
                        preco = litros*2.50 - litros*2.50*0.05
                self.preco_total.set(round(preco, 2))
        except:
                self.parent.geometry("380x230+50+35")
                self.preco_total.set("ERRO!\nVerifique o valor digitado")
                self.preco_total_exit["foreground"] = "red"
                self.preco_total_exit["font"] = "Arial 8 bold"
                self.preco_total_exit["anchor"] = "center"
                self.preco_total_exit["justify"] = "center"
                self.preco_total_exit["width"] = "25"


          
peso_ideal = My_class()
