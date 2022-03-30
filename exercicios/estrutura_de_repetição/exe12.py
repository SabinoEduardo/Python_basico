#
#? Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
#* Tabuada de 5:
#* 5 X 1 = 5
#* 5 X 2 = 10
...
#* 5 X 10 = 50

i = 1
numero = float(input("Digite um número:"))
print(f'{"Tabuada de ":>30}{numero}')
print("-"*60)
while i <= 10:
    print(f"{numero} X {i:>2} = {numero*i}")
    i += 1