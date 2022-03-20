#
#* Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.


from tkinter import *
from tkinter import ttk

class Loja_Tintas():
    def __init__(self):

        self.parents = Tk()
        self.parents.title("Loja de Tintas")
        self.parents.geometry("370x280+30+30")
        self.parents.resizable(0, 0)
        self.frame_1 = ttk.Frame(self.parents, border=1, relief=SOLID, padding=(10, 10))
        self.frame_2 = ttk.Frame(self.parents, border=1, relief=SOLID, padding=(10, 10))

        #* Variaveis
        self.area_parede = StringVar()
        self.qtde_latas = StringVar()

        #* widgets
        self.text_areaValue = ttk.Label(self.frame_1, text="Área da parede(m²):", font="Arial 9 bold")
        self.entrada_areaValue = ttk.Entry(self.frame_1, textvariable=self.area_parede, justify="center")

        self.text_qtdeLatas = ttk.Label(self.frame_1, text="Quantidade de Latas:", font="Arial 9 bold", justify="center")
        self.saida_qtdeLatas = ttk.Label(self.frame_1, textvariable=self.qtde_latas, background="#ccccb3",
                                            justify="center", width=20)

        self.mensagem = ttk.Label(self.frame_2, text="Nota:",  justify="right", anchor="w", font="Arial 12 bold")
        self.mensage_saida = ttk.Label(self.frame_2, text="1 litro de tinta cobre 3 metros quadrados.\nAs latas possuem 18 litros e que custam R$ 80,00.", justify="left", anchor="w", font="Arial 10 normal")

        btn = Button(self.parents, text="Calcular", background="#000000", foreground="#f2f2f2", width=10, font="Arial 10 bold",
                        command=self.calcular)

        #* Layout
        self.frame_1.grid(padx=45, pady=20)
        self.frame_2.grid(row=2, column=0, pady=15)

        self.text_areaValue.grid(row=0, column=0, padx=10, pady= 10)
        self.entrada_areaValue.grid(row=0, column=1)

        self.text_qtdeLatas.grid()
        self.saida_qtdeLatas.grid(row=1, column=1, pady= 10)

        btn.grid(row=1, column=0)

        self.mensagem.grid(padx=8)
        self.mensage_saida.grid()

        self.parents.mainloop()

    def calcular(self):
        #! 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00
        #* Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

        qtde_litros = float(self.area_parede.get())/3
        qtde_latas = qtde_litros/18
        self.qtde_latas.set(qtde_latas)


loja_de_tintas = Loja_Tintas()