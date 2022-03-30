#
#? Faça um programa que leia e valide as seguintes informações:
#* Nome: maior que 3 caracteres;
#* Idade: entre 0 e 150;
#* Salário: maior que zero;
#* Sexo: 'f' ou 'm';
#* Estado Civil: 's', 'c', 'v', 'd';

while True:
    name = str(input("Name: "))
    age = int(input("Age: "))
    salary = float(input("Salary: "))
    sex = str(input("Sex: ")).upper()[0]
    marital_status = str(input("Marital status: ")).upper()[0]
    if (len(name) > 3) and (age >= 0 and age <= 150) and salary > 0 and (sex in ("M", "F")) and (marital_status in ("S", "C", "V", "D")):
        print("Dados corretos")
        break
    else:
        print("Error!\nVerifique os dados digitados")