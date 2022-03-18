# Faça um Programa que peça dois números e imprima a soma.

from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Soma de dois números")
root.geometry("350x150+30+30")

minha_frame1 = Frame(root)
minha_frame2 = Frame(root)

# Função

def soma():
    try:
        n1 = float(var1_entrada.get())
        n2 = float(var2_entrada.get())
        label_saida["fg"] = "black"
        var_saida.set(round((n1 + n2), 2))
    except:
        label_saida["fg"] = "red"
        var_saida.set("ERRO!\nVerifique os valores digitados.")
    

#Variaveis

var1_entrada = StringVar()
var2_entrada = StringVar()
var_saida = StringVar()

#Widgets
label_var1 = Label(minha_frame1, text="Número1:")
entrada_var1 = ttk.Entry(minha_frame1, textvariable=var1_entrada, width=37)
label_var2 = Label(minha_frame1, text="Número2:")
entrada_var2 = ttk.Entry(minha_frame1, textvariable=var2_entrada, width=37)
label_text = Label(minha_frame2, text="Resultado:")
label_saida = Label(minha_frame2, textvariable=var_saida , bg="#ccccb3", width=27, font="Arial 10 bold")
btn = Button(minha_frame2, text="somar", command=soma)

#Layout
label_var1.grid(row=0, column=0, padx=3, pady=3)
entrada_var1.grid(row=0, column=1)
label_var2.grid(row=1, column=0)
entrada_var2.grid(row=1, column=1)
label_text.grid(row=0, column=0, padx=2)
label_saida.grid(row=0, column=1, padx=2)
btn.grid(row=1, column=1, pady=10)

minha_frame1.grid(row=0, column=0, padx=12, pady=12)
minha_frame2.grid(row=2, column=0, padx=12)

entrada_var1.focus()

root.mainloop()