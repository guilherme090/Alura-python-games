# Este projeto está diferente daquele sugerido pelo curso
def chute_eh_valido(chute):
    if(not chute.isnumeric()):
        return False
    if(int(chute) < 1 or int(chute) > 100):
        return False
    return True

def nivel_eh_valido(nivel):
    if(not nivel.isnumeric()):
        return False
    if(int(nivel) < 1 or int(nivel) > 3):
        return False
    return True
    
def jogar():

    import random

    numero_secreto = random.randrange(1,101)
    rodada = 1
    ganhou = False
    nivel = 'Vazio'
    pontos = 0    

    print('\n\nBem-vindo ao jogo de adivinhação, jogador!')

    while(nivel_eh_valido(nivel) == False):
        nivel = input('Escolha o nível de dificuldade. 1 - Fácil, 2 - Médio, 3 - Difícil: ')

    nivel = int(nivel)
    if(nivel == 1):
        tentativas = 20
    elif(nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    pontos = 99 * tentativas

    while(rodada <= tentativas):
        # print(f'Tentativa {rodada} de {TENTATIVAS_TOTAL}')
        print('\nTentativa {:02d} de {:02d}'.format(rodada, tentativas))
        chute = input("Digite um número entre 1 e 100: ")

        if(not chute_eh_valido(chute)):
            print('Você precisa digitar um número entre 1 e 100 para que o jogo funcione.')
            continue
        else:
            chute = int(chute)

            chutou_para_mais = chute > numero_secreto
            chutou_para_menos = chute < numero_secreto
            ganhou = False
            pontos = pontos - abs(numero_secreto - chute)

            if(chutou_para_mais):
                print('Você errou. O seu chute foi maior que o número secreto.')
                rodada = rodada + 1
            elif(chutou_para_menos):
                print('Você errou. O seu chute foi menor que o número secreto.')
                rodada = rodada + 1
            else:
                ganhou = True
                print('Parabéns, você acertou!')
                break

    print('\nFim de jogo. O número secreto era {:d}.'.format(numero_secreto))
    print(f'Você fez {pontos} pontos.')

if(__name__ == "__main__"):
    jogar()