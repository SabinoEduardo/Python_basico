from random import randint


def jogo_advinhacao():
    mensagem_inicial()
    numero_tentativas = escolha_nivel()
    contador = 0
    numero = randint(0, 10)
    while True:
        print(f'Você tem {numero_tentativas - contador} tentativas')
        chute = input('Digite um número:')
        print()
        if chute.isnumeric():
            acertou = numero == int(chute)
            if acertou:
                print('Você acertou')
                print(f'Foram {contador+1} tentativas')
                break
            maior = int(chute) > numero
            print('Você errou')
            print("Você chutou para cima") if maior else print("Você chutou para baixo")
            contador += 1
            print()
            if contador == numero_tentativas:
                print('Você perdeu!')
                break
        else:
            print('Valor digitado não é um número')
    print()
    continuar_jogando()


def mensagem_inicial():
    print('*' * 30)
    print(f'{"Bem Vindo ao Jogo da Advinhação":>28}')
    print('*' * 30)


def escolha_nivel():
    print('Escolha o nível')
    print(f'{"1 - Fácil":>15}')
    print(f'{"2 - Médio":>15}')
    print(f'{"3 - Avançado":>18}')
    nivel = input('Nível: ')
    print('-' * 30)
    options = [1, 2, 3]
    if not nivel.isnumeric() or int(nivel) not in options:
        print('ERRO!\nVerifique a sua escolha\n')
        escolha_nivel()
    else:
        nivel = int(nivel)
        if nivel == 1:
            tentativas = 20
            nivel = 'Fácil'
        elif nivel == 2:
            tentativas = 10
            nivel = 'Médio'
        else:
            tentativas = 5
            nivel = 'Avançado'
        print (f'Nivel: {nivel}')
        return tentativas

        
def continuar_jogando():
    while True:
        option_continue = input('Desejas continuar[Y/N]?')
        print()
        if option_continue not in 'YyNn':
            print()
            print('Respostas possiveis:')
            print(f'{"Continuar Jogando[Y]":>24}')
            print(f'{"Não Continuar[N]":>20}')
        else:
            if option_continue in 'Yy':
                jogo_advinhacao()
            else:
                break


if __name__ == '__main__':
    jogo_advinhacao()
    print('Fim do Jogo')
