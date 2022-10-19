# coding=utf-8
import advinhacao
import forca


def escolha_jogo():
    print('Bem vindo ao meu programa de jogos')
    while True:
        print()
        print('Opcões de Jogo')
        print(f'{"[1] - Jogo da Forca":>22}')
        print(f'{"[2] - Jogo de Advinhaçâo":>27}')
        print(f'{"[3] - Desligar o Programa":>28}')
        option = input('Escolha um jogo:')
        print()
        if option.isnumeric():
            option = int(option)
            if option == 1:
                forca.jogo_forca()
            elif option == 2:
                advinhacao.jogo_advinhacao()
            elif option == 3:
                break
        print('Opção de jogo Errada!')
    print('Encerrando o programa')


escolha_jogo()
