from random import randrange


def jogo_forca():
    jogar = True
    while jogar:
        mensagem_inicial()
        palavra_secreta = carrega_palavra_secreta()
        palavra = ["_" for _ in palavra_secreta]
        erros = 0
        tentativas = 7
        while True:
            print(f'Você tem {tentativas - erros} tentativas')
            chute = input('Letra:').strip().upper()
            if validar_letra(chute, palavra, palavra_secreta):
                print(validar_letra(chute, palavra, palavra_secreta))
                print()
            else:
                erros += 1
                desenha_forca(erros)
            if erros == 7:
                imprime_mensagem_perdedor(palavra_secreta)
                break
            else:
                if '_' not in palavra:
                    imprime_mensagem_vencedor()
                    break
        print()
        jogar = continuar_jogando()


def mensagem_inicial():
    print('*' * 30)
    print(f'{"Bem Vindo ao Jogo da forca":>28}')
    print('*' * 30)


def carrega_palavra_secreta():
    lista_palavras = list()
    with open('arquivo.txt', 'r') as file:
        for f in file:
            f = f.strip()
            lista_palavras.append(f)
    indice = randrange(0, len(lista_palavras))
    palavra_secreta = lista_palavras[indice].upper()
    return palavra_secreta


def validar_letra(chute, palavra, palavra_secreta):
    if not chute.isalpha():
        return 'A entrada deve ser apenas letra'
    elif chute in palavra_secreta:
        for i, letter in enumerate(palavra_secreta):
            if chute == letter:
                palavra[i] = chute
        return palavra


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    elif erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    elif erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    elif erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    elif erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    elif erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    else:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def continuar_jogando():
    while True:
        option = input('Desejas continuar[Y/N]?')
        if option not in 'YyNn':
            print()
            print('Respostas possiveis:')
            print(f'{"Continuar Jogando[Y]":>24}')
            print(f'{"Não Continuar[N]":>20}')
        else:
            if option in 'Yy':
                jogar = True
            else:
                jogar = False
            break
    return jogar


if __name__ == '__main__':
    jogo_forca()
    print('Fim do Jogo')
