
def linha():
    print(20 * '=')


def menu():
    linha()
    print('Embaralha Palavra')
    linha()


def dificuldade():

    dificuldades = ['facil', 'medio', 'dificil']

    print('Escolha a dificuldade:')
    print('1 - Fácil')
    print('2 - Médio')
    print('3 - Difícil')
    linha()

    escolha_dificuldade = int(input('Escolha: '))

    if escolha_dificuldade > 3 or escolha_dificuldade < 1:
        print('Dificuldade inválida! Tente novamente.')
        dificuldade()

    return print(dificuldades[escolha_dificuldade-1])


def tema():

    temas = ['animais', 'paises', 'cidades']

    linha()
    print('Escolha o tema:')
    print('1 - Animais')
    print('2 - Países')
    print('3 - Cidades')
    linha()

    escolha_tema = int(input('Escolha: '))

    if escolha_tema > 3 or escolha_tema < 1:
        print('Tema inválido! Tente novamente.')
        tema()

    return print(temas[escolha_tema-1])


menu()
dificuldade()
tema()
