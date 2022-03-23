#
#?Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#* a) A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#* b) A mensagem "Reprovado", se a média for menor do que sete;
#* c) A mensagem "Aprovado com Distinção", se a média for igual a dez.

#! Será usado o módulo Tkinter para a resolção deste problema

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class My_Class():
    def __init__(self):

        #* Criate tkinter object and my_frame.
        self.parent = Tk()
        self.parent.title("Nota Média e Situação do Aluno")
        self.parent.geometry("400x240+30+30")
        self.my_frame = ttk.Frame(self.parent, border=2, relief=SOLID, padding=(10))

        #* My variables
        self.nota1 = StringVar()
        self.nota2 = StringVar()
        self.media = StringVar()
        self.situacao = StringVar()

        #* Create my widgets
        self.text_nota1 = ttk.Label(self.my_frame, text="Nota1:", font="Arial 10 bold")
        self.input_nota1 = ttk.Entry(self.my_frame, textvariable=self.nota1, width=22, justify="center", 
                                    font="Arial 10 bold")

        self.text_nota2 = ttk.Label(self.my_frame, text="Nota2:", font="Arial 10 bold")
        self.output_nota2 = ttk.Entry(self.my_frame, textvariable=self.nota2, width=22, justify="center",
                                         font="Arial 10 bold")

        self.text_media = ttk.Label(self.my_frame, text="Média:", font="Arial 10 bold")
        self.output_media = ttk.Label(self.my_frame, textvariable=self.media, background="#ccccb3", 
                                        width=22, anchor="center", justify="center", font="Arial 10 bold")

        self.text_situacao = ttk.Label(self.my_frame, text="Situação:", 
                                        font="Arial 10 bold")

        self.output_situacao = ttk.Label(self.my_frame, textvariable=self.situacao, background="#ccccb3",
                                        width=22, anchor="center", justify="center", 
                                        font="Arial 10 bold")

        self.btn = Button(self.parent, text="Calcular Média", width=15, background="#ff6666",
                            font="Arial 12 bold", command=self.media_situacao)

        self.my_frame.grid(row=0, column=0, padx=75, pady=20)

        self.text_nota1.grid(row=0, column=0)
        self.input_nota1.grid(row=0, column=1)

        self.text_nota2.grid(row=1, column=0, pady=10)
        self.output_nota2.grid(row=1, column=1)

        self.text_media.grid(row=2, column=0)
        self.output_media.grid(row=2, column=1)

        self.text_situacao.grid(row=3, column=0)
        self.output_situacao.grid(row=3, column=1, padx=3, pady=10)

        self.btn.grid(row=1)

        self.input_nota1.focus()

        self.parent.mainloop()

    def media_situacao(self):
        try:
            n1 = float(self.nota1.get())
            n2 = float(self.nota2.get())
            media = (n1 + n2)/2
            self.media.set(round(media, 2))
            if media >= 7:
                self.output_situacao["foreground"] = "blue"
                if media == 10:
                    self.situacao.set("Aprovado com distinção")
                else:
                    self.situacao.set("Aprovado")

            else:
                self.output_situacao["foreground"] = "red"
                self.situacao.set("Reprovado")
        except:
            messagebox.showerror("Mensagem de erro", "Verifique o valor salário.")
         
notas_situação = My_Class()
