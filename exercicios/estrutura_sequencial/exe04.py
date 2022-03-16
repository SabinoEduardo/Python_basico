#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

from tkinter import *

# Class

class media_nota():

# Função
    def __init__(self):

        #Criando objeto Tkinter, definindo o titulo e a geometria
        self.root = Tk()
        self.root.title("Média entre 4 notas")
        self.root.geometry("400x150+40+40")

        #Frames
        self.frame_entrada = Frame(self.root)
        self.minha_frame1 = Frame(self.frame_entrada)
        self.minha_frame2 = Frame(self.frame_entrada)
        self.minha_frame3 = Frame(self.root)

        #Variaveis
        self.var_num1 = StringVar()
        self.var_num2 = StringVar()
        self.var_num3 = StringVar()
        self.var_num4 = StringVar()
        self.var_media = StringVar()

        # Widgets
        self.label_num1 = Label(self.minha_frame1, text="Nota1:")
        self.entrada_num1 = Entry(self.minha_frame1, textvariable=self.var_num1)

        self.label_num2 = Label(self.minha_frame2, text="Nota2:")
        self.entrada_num2 = Entry(self.minha_frame2, textvariable=self.var_num2)

        self.label_num3 = Label(self.minha_frame1, text="Nota3:")
        self.entrada_num3 = Entry(self.minha_frame1, textvariable=self.var_num3)

        self.label_num4 = Label(self.minha_frame2, text="Nota4:")
        self.entrada_num4 = Entry(self.minha_frame2, textvariable=self.var_num4)

        self.label_media_text = Label(self.minha_frame3, text="Média:")
        self.label_media_res = Label(self.minha_frame3, textvariable=self.var_media, 
                                        width=16, bg="#ccccb3", font="Arial 10 bold")

        self.btn = Button(self.minha_frame3, text="salvar", command=self.media)
        self.label_erro = Label(self.root, text=" ", fg="red", font="Arial 10 bold")

        # Layouts das frames

        self.frame_entrada.grid(row=0, columnspan=1)
        self.minha_frame1.grid(row=0, column = 0, padx=20, pady=15)
        self.minha_frame2.grid(row=0, column=1)
        self.minha_frame3.grid(row=1, column=0)

        #layout das Labels e Entry
        self.label_num1.grid(row=0, column=0)
        self.entrada_num1.grid(row=0, column=1)

        self.label_num2.grid(row=0, column=2)
        self.entrada_num2.grid(row=0, column=3)

        self.label_num3.grid(row=1, column=0)
        self.entrada_num3.grid(row=1, column=1)

        self.label_num4.grid(row=1, column=2)
        self.entrada_num4.grid(row=1, column=3)

        self.label_media_text.grid(row=2, column=0, padx=5)
        self.label_media_res.grid(row=2, column=1)
        self.btn.grid(row=3, column=1, padx=15, pady=15)
        self.label_erro.grid()

        # Focus
        self.entrada_num1.focus()

        #metodo mainliip
        self.root.mainloop()

    # Função para calcular a média entre as 4 notas
    def media(self):
        try:
            self.root.geometry("400x150+40+40")
            self.label_erro["text"] = " "
            soma =(float(self.var_num1.get()) + float(self.var_num2.get()) + 
                    float(self.var_num3.get()) + float(self.var_num4.get()))
            self.var_media.set(round((soma/4), 2))
        except:
            self.label_erro["text"] = "Erro!\nVerifique os valores digitados e tente novamente."
            self.var_media.set(" ")
            self.root.geometry("400x250+40+40")

# Criando objeto          
notas = media_nota()
