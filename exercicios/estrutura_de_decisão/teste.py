numero = 16


if numero < 10:
    unidade = numero
elif numero < 100:
    dezena = numero//10
    dezena = (numero - dezena*10)
elif numero < 100:
    centena = numero//100
    dezena = numero - centena*100
    unidade = numero - centena*100 - centena*10

print(centena)
print(dezena)
print(unidade)
