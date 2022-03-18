#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.


from tkinter import *
from tkinter import ttk
from math import pi

class Area_circulo():
    def __init__(self):

        # Criando um objeto tkinter, definindo a geometria e o título.

        self.root = Tk()
        self.root.title("Área de um círculo")
        self.root.geometry("350x150")
        self.root.resizable(0, 0)

        # Frame
        self.minha_frame = ttk.Frame(self.root, padding=(65, 20, 90, 10))
        

        #Variaveis
        self.var1_raio = StringVar()
        self.var2_area = StringVar()

        #Widgets
        self.label_raio = Label(self.minha_frame, text="Raio:")
        self.entrada_raio = Entry(self.minha_frame, textvariable=self.var1_raio, width=25)

        self.label_area = Label(self.minha_frame, text="Área:")
        self.saida_area = Label(self.minha_frame, textvariable=self.var2_area, width=21, background="#ccccb3")

        self.btn = ttk.Button(self.root, text="Calcular", command=self.area)
        self.label_erro = Label(self.root, text=" ", fg="red", font="Arial 10 bold")

        #Layout
        self.minha_frame.grid(row=0, column=0) 
        

        self.label_raio.grid(row=0, column=0, padx=3, pady=3)
        self.entrada_raio.grid(row=0, column=1)

        self.label_area.grid(row=1, column=0)
        self.saida_area.grid(row=1, column=1)

        self.btn.grid(columnspan=2, padx=30, pady=10)
        self.label_erro.grid(padx=10, pady=10)


        self.root.mainloop() # Metodo mainloop

    def area(self):
        """
            Função para calcular o valor da área de um círculo 
        """
        try:
            self.root.geometry("350x150")
            self.raio = float(self.var1_raio.get())
            self.var2_area.set(round(((self.raio)**2)*pi, 2))
            self.label_erro["text"] = " "
        
        except:
            self.root.geometry("350x200")
            self.label_erro["text"] = "Erro!\nVerifique os valores digitados e tente novamente."
            self.var2_area.set(" ")
           


area_circulo = Area_circulo() # Criando um objeto da classe Area_circulo