from random import randint


def jogo_advinhacao():
    mensagem_inicial()
    numero_tentativas = escolha_nivel()
    count = 1
    numero = randint(0, 10)
    print(f'Você tem {numero_tentativas} tentativas')
    while count <= numero_tentativas:
        chute = input('Digite um número:')
        print()
        if chute.isnumeric():
            acertou = numero == int(chute)
            if acertou:
                print('Você acertou')
                print(f'Foram {count} tentativas')
                break
            maior = int(chute) > numero
            print('Você errou')
            print("Você chutou para cima") if maior else print("Você chutou para baixo")
            count += 1
            print(f'Você tem {numero_tentativas-count} tentativas')
            print()

        else:
            print('Valor digitado não é um número')
    continuar_jogando()


def mensagem_inicial():
    print('*' * 30)
    print(f'{"Bem Vindo ao Jogo da Advinhação":>28}')
    print('*' * 30)


def escolha_nivel():
    print('Escolha o nível')
    print('1 - Fácil\n2 - Médio\n3 - Avançado')
    nivel = input('Nível: ')
    print('-' * 30)
    if nivel.isnumeric():
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
        print(f'Nivel {nivel}')
        return tentativas
    print('ERRO!\nVerifique a sua escolha')
    print()
    escolha_nivel()


def continuar_jogando():
    while True:
        option = input('Desejas continuar[Y/N]?')
        print()
        if option not in 'YyNn':
            print()
            print('Respostas possiveis:')
            print(f'{"Continuar Jogando[Y]":>24}')
            print(f'{"Não Continuar[N]":>20}')
        else:
            if option in 'Yy':
                jogo_advinhacao()
            else:
                break


if __name__ == '__main__':
    jogo_advinhacao()
    print('Fim do Jogo')
