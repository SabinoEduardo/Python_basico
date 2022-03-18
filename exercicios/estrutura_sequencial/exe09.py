# Faça um Programa para conversão de temperatura.
# Opção de converter de graus Celsius para graus Fahrenheit
# e de graus Fahrenheit para graus Celsius


from tkinter import *
from tkinter import ttk


class Temperature_Convert():
    def __init__(self):

        # Criate parent object tk e as frames
        self.parent = Tk()
        self.parent.title("Conversor de temperatura")
        self.my_frame1 = ttk.Frame(self.parent, padding=(60, 10, 50, 10), width=40)
        self.my_frame2 = ttk.Frame(self.parent, padding=(60, 10, 50, 10), width=40)
        self.parent.geometry("350x230+40+35")
        self.parent.resizable(1, 0)
        

        # Variables
        self.option = IntVar()   
        self.input_value = StringVar()  
        self.exit_value = StringVar()

        # Widgets

        self.text_radio = ttk.Label(self.my_frame1, text="Selecione uma opção", font="Arial 12 bold")
        self.celsios_fahrenheit = ttk.Radiobutton(self.my_frame1, text='Celsius para Fahrenheit', variable=self.option, value=1)
        self.fahrenheit_celsius = ttk.Radiobutton(self.my_frame1, text='Fahrenheit para Celsius', variable=self.option, value=0)

        self.text_entrada = ttk.Label(self.my_frame2, text="Valor Entrada:", font="Arial 9 bold")
        self.temperature_entry = ttk.Entry(self.my_frame2, justify="center", textvariable=self.input_value)

        self.text_saida = ttk.Label(self.my_frame2, text="Valor Saida:", font="Arial 9 bold")
        self.temperature_exit = ttk.Label(self.my_frame2, background="#ccccb3", textvariable=self.exit_value, width=17, font="Arial 10 bold")

        self.buton = Button(self.parent, text="Converte", command=self.temperatura_convert, width=10, background="#ff3333", font="Arial 10 bold")

        # Layout
        self.my_frame1.grid(row=0, column=1)
        self.my_frame2.grid(row=1, column=1)
        self.text_radio.grid()
        self.celsios_fahrenheit.grid()
        self.fahrenheit_celsius.grid()

        self.text_entrada.grid(row=1)
        self.temperature_entry.grid(row=1, column=1)

        self.text_saida.grid(pady=15)
        self.temperature_exit.grid(row=2, column=1)

        self.buton.grid(row=2, column=1, pady=3)

        self.temperature_entry.focus()
        
        self.parent.mainloop()
        

    def temperatura_convert(self):
        """
            Função para converter a temperatuda de uma unidade para outra.
        """
        
        try:
            self.temperature_exit["foreground"] = "black"
            self.temperature_exit["font"] = "Arial 10 bold"
            self.temperature_exit["anchor"] = "center"
            self.temperature_exit["justify"] = "center"
            self.temperature_exit["width"] = "17"
            if self.option.get() == 1:
                self.exit_value.set(round(32 + (9 * float(self.input_value.get())/5), 2) )
            else:
                self.exit_value.set(round(5 * ((float(self.input_value.get())-32) / 9), 2) )
        except:
                self.exit_value.set("ERRO!\nVerifique o valor digitado")
                self.temperature_exit["foreground"] = "red"
                self.temperature_exit["font"] = "Arial 8 bold"
                self.temperature_exit["anchor"] = "center"
                self.temperature_exit["justify"] = "center"
                self.temperature_exit["width"] = "25"


          
temperature = Temperature_Convert()
