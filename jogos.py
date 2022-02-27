import adivinhacao
import forca

def escolhe_jogo():
    escolha = 0
    while(escolha != 1 and escolha != 2):
        escolha = input('Escolha o seu jogo: 1 - Adivinhação, 2 - Forca: ')
        if(type(escolha) == str and escolha.isnumeric()):
            escolha = int(escolha)

    if(escolha == 1):
        adivinhacao.jogar()
    elif(escolha == 2):
        forca.jogar()

if(__name__ == '__main__'):
    escolhe_jogo()