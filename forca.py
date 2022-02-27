import random

def carregar_arquivo(nome_do_arquivo='palavras.txt'):
    arquivo = open(nome_do_arquivo, 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    
    arquivo.close()

    # Forma alternativa que funciona mesmo se o arquivo não for fechado:
    # with open("palavras.txt") as arquivo:
    # for linha in arquivo:
    #     print(linha)
    return(palavras)

def inicializar_letras_acertadas(palavra_secreta):
    return ['_' for letra in palavra_secreta]

def imprime_mensagem_vencedor():
    print("\nParabéns, você ganhou!")
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

def imprime_mensagem_perdedor():
    print("\nPuxa, você foi enforcado!")
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

def desenha_forca(no_chances):
    erros = 7 - no_chances
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 0):
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprimir_letras_corretas(palavra_secreta, escolha, letras_acertadas, enforcou):
    index = 0
    ha_letra = False
    for letra in palavra_secreta:
            if(letra == escolha or enforcou == True):
                letras_acertadas[index] = letra
                ha_letra = True
            index += 1
    return ha_letra

def imprimir_letras_erradas(letras_erradas):
    print('Letras erradas: ', end=' ')
    if(len(letras_erradas) > 0):
        print(letras_erradas)

def jogar():

    print('\n\nBem-vindo ao jogo da Forca, jogador!')
    palavras = carregar_arquivo()
    palavra_secreta = palavras[random.randrange(0,len(palavras))].upper()
    letras_acertadas = inicializar_letras_acertadas(palavra_secreta) 
    letras_erradas = set()
    enforcou = False
    acertou = False
    no_chances = 7

    while (not enforcou and not acertou):
        print('jogando...')
        desenha_forca(no_chances)
        print('Palavra: ', letras_acertadas)
        imprimir_letras_erradas(letras_erradas)
        print('Tentativas restantes: ', no_chances)
        escolha = input('Escolha uma letra: ')
        escolha = escolha.strip().upper()

        ha_letra = imprimir_letras_corretas(palavra_secreta, escolha, letras_acertadas, enforcou)

        if(not ha_letra):
            letras_erradas.add(escolha)
            no_chances -= 1
        
        enforcou = no_chances == 0
        acertou = not '_' in letras_acertadas

    imprimir_letras_corretas(palavra_secreta, escolha, letras_acertadas, enforcou)
    print('\nPalavra: ', letras_acertadas)
    imprimir_letras_erradas(letras_erradas)
    print('Fim do jogo.', end=' ')

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()

if(__name__ == "__main__"):
    jogar()