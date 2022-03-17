# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
# Quadrado é uma figura geometrica com todos lados iguais. A = b*h => b = h = L => A = L^2

from tkinter import *
from tkinter import ttk
from math import pi

class Area_circulo():
    def __init__(self):

        # Criando um objeto tkinter, definindo a geometria e o título.

        self.root = Tk()
        self.root.title("Dobro da área de um quadrado.")
        self.root.geometry("350x150")
        self.root.resizable(0, 0)

        # Frame
        self.minha_frame = ttk.Frame(self.root, padding=(65, 20, 90, 10))

        #Variaveis
        self.var1_comprimento = StringVar()
        self.var2_dobro_quadrado = StringVar()

        #Widgets
        self.label_comprimento = ttk.Label(self.minha_frame, text="Lado (metro):")
        self.entrada_comprimento = ttk.Entry(self.minha_frame, textvariable=self.var1_comprimento, width=25)

        self.label_dobro_quadrado = ttk.Label(self.minha_frame, text="Dobro da área:")
        self.saida_dobro_quadrado = ttk.Entry(self.minha_frame, textvariable=self.var2_dobro_quadrado, width=25)

        self.btn = ttk.Button(self.root, text="Calcular", command=self.area)
        self.label_erro = Label(self.root, text=" ", fg="red", font="Arial 10 bold")

        #Layout
        self.minha_frame.grid(row=0, column=0) 
        

        self.label_comprimento.grid(row=0, column=0, padx=3, pady=3)
        self.entrada_comprimento.grid(row=0, column=1)

        self.label_dobro_quadrado.grid(row=1, column=0)
        self.saida_dobro_quadrado.grid(row=1, column=1)

        self.btn.grid(columnspan=2, padx=30, pady=10)
        self.label_erro.grid(padx=10, pady=10)

        self.entrada_comprimento.focus()


        self.root.mainloop() # Metodo mainloop

    def area(self):
        """
            Função para calcular o valor da área de um círculo 
        """
        try:
            self.root.geometry("350x150")
            self.raio = float(self.var1_comprimento.get())
            self.var2_dobro_quadrado.set(round(((self.comprimento)**2)*2, 2))
            self.label_erro["text"] = " "
        
        except:
            self.root.geometry("350x200")
            self.label_erro["text"] = "Erro!\nVerifique os valores digitados e tente novamente."
            self.var2_area.set(" ")
           


area_circulo = Area_circulo() # Criando um objeto da classe Area_circulo