# Faça um Programa que peça um número e então mostre a       mensagem O número informado foi [número].

from tkinter import *

#GUI

root = Tk()
root.title("Mostrar o número digitado")
root.geometry("270x100+30+30")

#função
def mostrar_numero():
    label_saida = Label(root, text= "O número informado foi " + var_num.get())

    label_saida.grid(row=1, column=1)

#variavel
var_num = StringVar()

#widget
label1 = Label(root, text="Digite um numero:")
entrada_numero = Entry(root, textvariable=var_num)
btn = Button(root, text="Clica", command=mostrar_numero)

#layout
root.grid()
label1.grid(row=0, column=0)
entrada_numero.grid(row=0, column=1)
btn.grid(row=2, column=1)

root.mainloop()