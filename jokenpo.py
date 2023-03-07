from random import randint
from time import sleep
from emoji import emojize

lista = ['Pedra', 'Papel', 'Tesoura']

pontos_jogador = 0
pontos_computador = 0

jogar_novamente = "sim"

while jogar_novamente.lower() == "sim":
    computador = randint(0, 2)
    print('Jokenpo vs Computador')
    print(emojize('''Faça a sua escolha:
        [1] PEDRA :raised_fist:
        [2] PAPEL :hand_with_fingers_splayed:
        [3] TESOURA :victory_hand:'''))
    opcoes = [1, 2, 3]
    jogador = int(input('Sua opção: '))
    while jogador not in opcoes:
        jogador = int(input('Digite um valor válido [1, 2 ou 3]. Qual é a sua jogada? '))

    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    sleep(1)

    if computador == 0:
        print(emojize('O computador escolheu {} :raised_fist:'.format(lista[computador])))
        if jogador == 1:
            print(emojize('''Você escolheu :raised_fist:
                  \033[1;33mEMPATE\033[0m'''))
        elif jogador == 2:
            print(emojize('''Você escolheu Papel :hand_with_fingers_splayed:
                  \033[1;32mVOCÊ VENCEU!\033[0m'''))
            pontos_jogador += 1
        elif jogador == 3:
            print(emojize('''Você escolheu Tesoura :victory_hand:
                  \033[1;31mCOMPUTADOR VENCE\033[0m'''))
            pontos_computador += 1
        else:
            print('Jogada inválida')
    elif computador == 1:
        print(emojize('O computador escolheu {} :hand_with_fingers_splayed:'.format(lista[computador])))
        if jogador == 1:
            print(emojize('''Você escolheu Pedra :raised_fist:
                   \033[1;31mCOMPUTADOR VENCE\033[0m'''))
            pontos_computador += 1
        elif jogador == 2:
            print(emojize('''Você escolheu Papel :hand_with_fingers_splayed:
                   \033[1;33mEMPATE\033[0m'''))
        elif jogador == 3:
            print(emojize('''Você escolheu Tesoura :victory_hand:
                   \033[1;32mVOCÊ VENCEU!\033[0m'''))
            pontos_jogador += 1
        else:
            print('Jogada inválida')
    elif computador == 2:
        print(emojize('O computador escolheu {} :victory_hand:'.format(lista[computador])))
        if jogador == 1:
            print(emojize('''Você jogou Pedra :raised_fist:
                  \033[1;32mVOCÊ VENCEU!\033[0m'''))
            pontos_jogador += 1
        elif jogador == 2:
            print(emojize('''Você escolheu Papel :hand_with_fingers_splayed:
                  \033[1;31mCOMPUTADOR VENCE\033[0m'''))
            pontos_computador += 1
        elif jogador == 3:
            print(emojize('''Você escolheu Tesoura :victory_hand:
                \033[1;33mEMPATE\033[0m'''))
        else:
           print('Jogada inválida')

    jogar_novamente = input("Deseja jogar novamente? (sim/não)")

    while jogar_novamente.lower() not in ["sim", "n", "nao"]:
       jogar_novamente = input("Resposta inválida. Deseja jogar novamente? (sim/não)")

    if jogar_novamente.lower() in ["n", "nao", "nao"]:
     print("Obrigado por jogar!")
     print("Pontuação final:")
     print("Jogador:", pontos_jogador)
     print("Computador:", pontos_computador)
     break
