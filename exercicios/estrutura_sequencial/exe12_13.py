# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7


#! O exercício 12 e 13 são iguais.


from tkinter import *
from tkinter import ttk

from click import option


class My_class():
    def __init__(self):

        # Criate parent object tk e as frames
        self.parent = Tk()
        self.parent.title("Calcular o peso ideal")
        self.my_frame1 = ttk.Frame(self.parent, padding=(60, 10, 50, 10), width=40)
        self.my_frame2 = ttk.Frame(self.parent, padding=(60, 10, 50, 10), width=40)
        self.parent.geometry("350x230+40+35")
        self.parent.resizable(1, 0)
        

        # Variables
        self.option = IntVar()   
        self.height_value = StringVar()
        self.wheigth_value = StringVar()  
        

        # Widgets

        self.text_radio = ttk.Label(self.my_frame1, text="Selecione uma opção", font="Arial 12 bold")
        self.male = ttk.Radiobutton(self.my_frame1, text='Homem', variable=self.option, value=1)
        self.female = ttk.Radiobutton(self.my_frame1, text='Mulher', variable=self.option, value=0)

        self.text_entrada = ttk.Label(self.my_frame2, text="Altura:", font="Arial 9 bold")
        self.height_value_entry = ttk.Entry(self.my_frame2, justify="center", textvariable=self.height_value)

        self.text_saida = ttk.Label(self.my_frame2, text="Peso:", font="Arial 9 bold")
        self.wheigth_value_exit = ttk.Label(self.my_frame2, background="#ccccb3", textvariable=self.wheigth_value, width=17, font="Arial 10 bold")

        self.buton = Button(self.parent, text="Converte", command=self.weigth_calculation, width=10, background="#ff3333", font="Arial 10 bold")


        # Layout
        self.my_frame1.grid(row=0, column=1)
        self.my_frame2.grid(row=1, column=1)
        self.text_radio.grid()
        self.female.grid()
        self.male.grid()
        
        self.text_entrada.grid(row=1)
        self.height_value_entry.grid(row=1, column=1)

        self.text_saida.grid(pady=15)
        self.wheigth_value_exit.grid(row=2, column=1)

        self.buton.grid(row=2, column=1, pady=3)

        self.height_value_entry.focus()
        
        self.parent.mainloop()
        

    def weigth_calculation(self):
        """
            Função para converter a temperatuda de uma unidade para outra.
        """
        
        try:
            self.wheigth_value_exit["foreground"] = "black"
            self.wheigth_value_exit["font"] = "Arial 10 bold"
            self.wheigth_value_exit["anchor"] = "center"
            self.wheigth_value_exit["justify"] = "center"
            self.wheigth_value_exit["width"] = "17"
            altura = float(self.height_value.get())

            if self.option.get() == 1:    
                self.wheigth_value.set(round( float( 72.7*altura - 58), 2))
            
            else:   
                self.wheigth_value.set(round(float(62.1*altura - 44.7), 2))
        except:
                self.wheigth_value.set("ERRO!\nVerifique o valor digitado")
                self.wheigth_value_exit["foreground"] = "red"
                self.wheigth_value_exit["font"] = "Arial 8 bold"
                self.wheigth_value_exit["anchor"] = "center"
                self.wheigth_value_exit["justify"] = "center"
                self.wheigth_value_exit["width"] = "25"


          
peso_ideal = My_class()
