#
#? Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#?a) A mensagem "Aprovado", se a média alcançada for maior ou igual  a sete;
#?b) A mensagem "Reprovado", se a média for menor do que sete;
#?c) A mensagem "Aprovado com Distinção", se a média for igual a dez.

#! Será usado o módulo Tkinter para a resolção deste problema


from cProfile import label
from tkinter import *
from tkinter import ttk

class My_Class():
    def __init__(self):

        #* Criate tkinter object and my_frame.
        self.parent = Tk()
        self.parent.title("Nota média e situação")
        self.parent.geometry("400x280+30+30")
        self.my_frame = ttk.Frame(self.parent, border=2, relief=SOLID, padding=(10))

        #* My variables
        self.nota_1 = StringVar()
        self.nota_2 = StringVar()
        self.media = StringVar()
        self.situacao = StringVar()

        #* Create my widgets
        self.text_nota1 = ttk.Label(self.my_frame, text="Nota 1:", font="Arial 10 bold")
        self.input_nota1 = ttk.Entry(self.my_frame, textvariable=self.nota_1, width=25, justify="center")

        self.text_nota2 = ttk.Label(self.my_frame, text="Nota 2:", font="Arial 10 bold")
        self.input_nota2 = ttk.Entry(self.my_frame, textvariable=self.nota_2, width=25, justify="center")

        self.text_media = ttk.Label(self.my_frame, text="Média:", font="Arial 10 bold")
        self.output_media = ttk.Label(self.my_frame, textvariable=self.media, background="#ccccb3", 
                                        width=25, anchor="center", justify="center", font="Arial 10 bold")

        self.btn = Button(self.parent, text="Calcular Média", width=15, background="#ff6666",
                            font="Arial 12 bold", command=self.media_situacao)

        self.my_frame.grid(row=0, column=0, padx=65, pady=20)

        self.text_nota1.grid(row=0, column=0)
        self.input_nota1.grid(row=0, column=1)

        self.text_nota2.grid(row=1, column=0, pady=10)
        self.input_nota2.grid(row=1, column=1)

        self.text_media.grid(row=2, column=0)
        self.output_media.grid(row=2, column=1)

        self.btn.grid(row=1)

        self.input_nota1.focus()

        self.parent.mainloop()

    def media_situacao(self):
        self.btn.grid(row=3)
        self.text_situacao = ttk.Label(self.parent, text="Situação:", 
                                        font="Arial 10 bold").grid(row=1, column=0)
        try:
            
            self.output_situacao = ttk.Label(self.parent, textvariable=self.situacao, background="#ccccb3",
                                        width=25, anchor="center", justify="center", 
                                        font="Arial 10 bold").grid(row=2, column=0, pady=10)

            n1 = float(self.nota_1.get())
            n2 = float(self.nota_2.get())
            media = (n1 + n2)/2
            self.media.set(round(media, 2))
            if media >= 7:
                if media == 10:
                    self.situacao.set("Aprovado com Distinção")
                else:
                    self.situacao.set("Aprovado")
            else:
            
                self.situacao.set("Reprovado")
        except:
            self.situacao.set("Verifique os valores digitados.")

#! analisar a parte da situação.
           


notas_situação = My_Class()
