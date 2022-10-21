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
        option_of_game = input('Escolha um jogo:')
        print()
        list_of_options = (1, 2, 3)
        if not option_of_game.isnumeric() or int(option_of_game) not in list_of_options:
            print('Opção de jogo Errada!')
        else:
            option_of_game = int(option_of_game)
            if option_of_game == 1:
                forca.jogo_forca()
            elif option_of_game == 2:
                advinhacao.jogo_advinhacao()
            elif option_of_game == 3:
                break
    print('Encerrando o programa')


escolha_jogo()
