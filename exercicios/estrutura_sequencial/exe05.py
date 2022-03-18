# Faça um Programa que converta metros para centímetros.

from tkinter import *

class Metros_Centimetros():
    def __init__(self):

        # Criando um objeto tkinter, definindo a geometria e o título.

        self.root = Tk()
        self.root.title("Converter metros para centimêtros")
        self.root.geometry("300x150")

        # Frame
        self.minha_frame = Frame(self.root)
        

        #Variaveis
        self.var1_metros = StringVar()
        self.var2_centimetros = StringVar()

        #Widgets
        self.label_metros = Label(self.minha_frame, text="Metros:")
        self.entrada_metros = Entry(self.minha_frame, textvariable=self.var1_metros, width=25)

        self.label_centimetros = Label(self.minha_frame, text="Centimetros:")
        self.saida_centimetros = Label(self.minha_frame, textvariable=self.var2_centimetros, width=21, background="#ccccb3")

        self.btn = Button(self.root, text="Converter", command=self.metros_centimetros)
        self.label_erro = Label(self.root, text=" ", fg="red", font="Arial 10 bold")

        #Layout
        self.minha_frame.grid(row=0, column=0, padx=12, pady=12)
        

        self.label_metros.grid(row=0, column=0, padx=3, pady=3)
        self.entrada_metros.grid(row=0, column=1)

        self.label_centimetros.grid(row=1, column=0)
        self.saida_centimetros.grid(row=1, column=1)

        self.btn.grid()
        self.label_erro.grid(padx=10, pady=10)


        self.root.mainloop() # Metodo mainloop

    def metros_centimetros(self):
        """
            Função para converter o valor de metro para centimetros e exibir o resultado na 
            label_centimetros.
        """
        try:
            self.root.geometry("300x150")
            self.centimetros = float(self.var1_metros.get())
            self.var2_centimetros.set(round(self.centimetros*100, 2))
            self.label_erro["text"] = " "
        except:
            self.root.geometry("350x200")
            self.label_erro["text"] = "Erro!\nVerifique os valores digitados e tente novamente."
            self.var2_centimetros.set(" ")


converte = Metros_Centimetros() # Criando um objeto da classe Metros_Centimetros