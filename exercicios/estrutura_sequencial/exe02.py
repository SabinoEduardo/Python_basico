# Faça um Programa que peça um número e então mostre a       mensagem O número informado foi [número].

from tkinter import *

#GUI

root = Tk()
root.title("Mostrar o número digitado")
root.geometry("270x100+30+30")

#função
def mostrar_numero():
    var_saida.set("O valor informado é: " + var_entrada.get())

    

#variavel
var_entrada = StringVar()
var_saida = StringVar()

#widget
label_text = Label(root, text="Digite um numero:")
entrada_numero = Entry(root, textvariable=var_entrada)
label_saida = Label(root, textvariable=var_saida)
btn = Button(root, text="Clica", command=mostrar_numero)

#layout
root.grid()
label_text.grid(row=0, column=0)
entrada_numero.grid(row=0, column=1)
label_saida.grid(row=1, column=1)
btn.grid(row=2, column=1)

root.mainloop()