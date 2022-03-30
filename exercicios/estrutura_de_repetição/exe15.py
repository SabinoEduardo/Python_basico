#
#? A série de Fibonacci é formada pela seqüência 0, 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.
print(f'{"Série de Fibonacci":>45}')
n = int(input("Quantidade de termos: "))
for i in range(1, n+1):
    if i == 1:
        primeiro_termo = 0
        print(primeiro_termo)
    elif i == 2:
        segundo_termo = 1
        print(segundo_termo)
    else:
        terceiro_termo = primeiro_termo + segundo_termo
        primeiro_termo = segundo_termo
        segundo_termo = terceiro_termo
        print(terceiro_termo)