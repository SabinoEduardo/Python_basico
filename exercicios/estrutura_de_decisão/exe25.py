#
#? Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

#* "Telefonou para a vítima?"
#* "Esteve no local do crime?"
#* "Mora perto da vítima?"
#* "Mora perto da vítima?"
#* "Já trabalhou com a vítima?"

#? O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

soma = 0
p1 = str(input("Telefonou para a vítima?\nR:")).upper()
if p1 == "SIM":
    soma += 1
p2 = str(input("Esteve no local do crime?\nR:")).upper()
if p2 == "SIM":
    soma += 1
p3 = str(input("Mora perto da vítima?\nR:")).upper()
if p3 == "SIM":
    soma += 1
p4 = str(input("Mora perto da vítima?\nR:")).upper()
if p4 == "SIM":
    soma+= 1
p5 = str(input("Já trabalhou com a vítima?\nR:")).upper()
if p5 == "SIM":
    soma += 1

if soma == 5:
    res = "Assassino"
elif soma >= 3:
    res = "Cúmplice"
elif soma == 2:
    res = "Suspeito"
else:
    res = "Inocente"


print(res)
