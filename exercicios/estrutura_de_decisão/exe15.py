#
#? Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#TODO - Dicas:
#* Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#* Triângulo Equilátero: três lados iguais;
#* Triângulo Isósceles: quaisquer dois lados iguais;
#* Triângulo Escaleno: três lados diferentes;

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import turtle

class My_Class():
    def __init__(self):

        #* Criate tkinter object and my_frame.
        self.parent = Tk()
        self.parent.title("Analise de triângulo")
        self.parent.geometry("400x270+30+30")
        self.my_frame = ttk.Frame(self.parent, border=2, relief=SOLID, padding=(10))

        #* My variables
        self.lado_a = StringVar()
        self.lado_b= StringVar()
        self.lado_c = StringVar()
        self.resultado = StringVar()

        #* Create my widgets
        self.text_lado_a = ttk.Label(self.my_frame, text="Lado a:", font="Arial 10 bold")
        self.input_lado_a = ttk.Entry(self.my_frame, textvariable=self.lado_a, width=22, justify="center", 
                                        font="Arial 10 bold")

        self.text_lado_b = ttk.Label(self.my_frame, text="Lado b:", font="Arial 10 bold")
        self.output_lado_b = ttk.Entry(self.my_frame, textvariable=self.lado_b, width=22, justify="center",
                                       font="Arial 10 bold")

        self.text_lado_c = ttk.Label(self.my_frame, text="Lado c:", font="Arial 10 bold")
        self.output_lado_c = ttk.Entry(self.my_frame, textvariable=self.lado_c, width=22, 
                                        justify="center", font="Arial 10 bold")

        self.text_resultado = ttk.Label(self.my_frame, text="Resultado:", 
                                        font="Arial 10 bold")

        self.output_resultado = ttk.Label(self.my_frame, textvariable=self.resultado, background="#ccccb3",
                                        width=25, anchor="center", justify="center", 
                                        font="Arial 10 bold", padding=5)

        self.btn = Button(self.parent, text="Resultado", width=15, background="#ff6666",
                            font="Arial 12 bold", command=self.analise_triagulo)

        self.my_frame.grid(row=0, column=0, padx=45, pady=20)

        self.text_lado_a.grid(row=0, column=0)
        self.input_lado_a.grid(row=0, column=1)

        self.text_lado_b.grid(row=1, column=0, pady=10)
        self.output_lado_b.grid(row=1, column=1)

        self.text_lado_c.grid(row=2, column=0)
        self.output_lado_c.grid(row=2, column=1)

        self.text_resultado.grid(row=3, column=0)
        self.output_resultado.grid(row=3, column=1, padx=3, pady=10)

        self.btn.grid(row=1)

        self.input_lado_a.focus()

        self.parent.mainloop()

    def analise_triagulo(self):
       
        try:
            self.a = float(self.lado_a.get())
            self.b = float(self.lado_b.get())
            self.c = float(self.lado_c.get())
            #self.output_resultado["width"] = 30
            #self.output_resultado["height"] = 20
            if self.a != 0 and self.b != 0 and self.c != 0:
                if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
                    if self.a == self.b == self.c:
                        self.n = 1
                        msg = "Os lados formam\ntriângulo Equilátero"

                    elif self.a == self.b or self.b == self.c or self.c == self.a:
                        self.n = 2
                        msg = "Os lados formam\ntriângulo Isósceles"

                    else:
                        self.n = 3
                        msg = "Os lados formam\ntriângulo Escaleno"

                    msg_box = messagebox.askquestion("Triângulo", f"{msg}\n\nVer o triângulo?")
                    if msg_box == "yes":
                        self.ver_triagulo()

                elif self.a + self.b == self.c or self.a + self.c == self.b or self.b + self.c == self.a:
                    self.resultado.set("Triângulo degenerado")

                else:
                    messagebox.showerror("Mensagem de erro", "Os valores dos lados informados\nnão formam triangulo")
            else:
                messagebox.showerror("Mensagem de erro", "Os valores dos lados informados\nnão formam triangulo")
        except:
            messagebox.showerror("Mensagem de erro", "Os valores dos lados informados\nnão formam triangulo")
    
    def ver_triagulo(self):
        self.resultado.set("sabino")
        triagulo = turtle.Turtle()
        print(triagulo)
        if self.n == 1:
            triagulo.fd(118*self.a)
            triagulo.lt(120)
            triagulo.fd(118*self.b)
            triagulo.lt(120)
            triagulo.fd(118*self.c)
        elif self.n == 2:
            if self.a == self.b:
                igual = self.a
                diferente = self.c
            elif self.a == self.c:
                igual = self.a
                diferente = self.b
            if self.b == self.c:
                igual = self.b
                diferente = self.a
            triagulo.fd(118*diferente)
            triagulo.lt(70*igual)
            triagulo.fd(118*igual)
            triagulo.lt(40*igual)
            triagulo.fd(118*igual)
        turtle.mainloop()
         
notas_situação = My_Class()

#! Terminar a criação dos triangulos.