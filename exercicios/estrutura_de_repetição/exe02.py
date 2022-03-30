#
#? Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    user = str(input("Username:"))
    passwoerd = str(input("Passaword:"))
    if user != passwoerd:
        print("User created successfully")
        break
    else:
        print("Error!\nThe password can´t be the same as the user")