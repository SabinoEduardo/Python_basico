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
import math

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
                        self.msg = "Os lados formam\ntriângulo Equilátero"

                    elif self.a == self.b or self.b == self.c or self.c == self.a:
                        self.n = 2
                        self.msg = "Os lados formam\ntriângulo Isósceles"

                    elif self.a != self.b and self.a != self.c and self.b != self.c:
                        self.n = 3
                        self.msg = "Os lados formam\ntriângulo Escaleno"
                    
                    else:
                        self.resultado.set("Triângulo degenerado")

            msg_box = messagebox.askquestion("Triângulo", f"{self.msg}\n\nVer o triângulo?")
            if msg_box in ("yes", "sim"):
                self.triagulo = turtle.Turtle()
                print(self.triagulo)
                
                self.opcao_triangulo()

        except:
            messagebox.showerror("Mensagem de erro", f"{self.n}, {msg_box} eduardo Os valores dos lados informados\nnão formam triangulo")
    

    def opcao_triangulo(self):
       
        if self.n == 1:
            self.equilatero()
        
        elif self.n == 2:
           self.isósceles()

        else:
            self.escaleno()
           
            
    def equilatero(self):
        self.triagulo.fd(118*self.a)
        self.triagulo.lt(120)
        self.triagulo.fd(118*self.b)
        self.triagulo.lt(120)
        self.triagulo.fd(118*self.c)

    def isósceles(self):
        if self.a == self.b:
            igual = self.a
            diferente = self.c
        elif self.a == self.c:
            igual = self.a
            diferente = self.b
        if self.b == self.c:
            igual = self.b
            diferente = self.a
        #* angulos interno
        angle_interno1 = 2*math.degrees(math.asin(diferente/(2*igual)))
        angle_interno2 = (180 - angle_interno1)/2 

        #* angulo externo
        angle_externo1 = (180 - angle_interno1)
        angle_externo2 = 180 - angle_interno2
        self.triagulo.fd(118*diferente)
        self.triagulo.lt(angle_externo2)
        self.triagulo.fd(118*igual)
        self.triagulo.lt(angle_externo1)
        self.triagulo.fd(118*igual)

    def escaleno(self):
        maior = menor  = medio = self.a
        #* maior número
        if self.b > maior:
            maior = self.b
        elif self.c > maior:
            maior = self.c

        #* menor número
        if self.b < menor:
            menor = self.b
        elif self.c < menor:
            menor = self.c

        #* médio número
        if self.b < maior and self.b > menor:
            medio = self.b
        elif self.c < maior and self.c > menor: 
            medio = self.c

        angle_interno1 = math.degrees(math.acos((maior**2 + menor**2 - medio**2)/(2*maior*menor)))
        angle_interno2 = math.degrees(math.acos((maior**2 + medio**2 - menor**2)/(2*maior*medio)))
        angle_interno3 = math.degrees(math.acos((menor**2 + medio**2 - maior**2)/(2*menor*medio)))
        self.triagulo.lt(angle_interno1)
        self.triagulo.fd(maior*59)
        self.triagulo.rt(180 - angle_interno2)
        self.triagulo.fd(medio*59)
        self.triagulo.rt(180 - angle_interno3)
        self.triagulo.fd(menor*59)
    
        turtle.mainloop()

notas_situação = My_Class()

#! Terminar a criação dos triangulos escaleno