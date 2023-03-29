from random import choice
from time import sleep
from emoji import emojize

options = {
    1: {'name': 'Pedra', 'emoji': ':raised_fist:'},
    2: {'name': 'Papel', 'emoji': ':hand_with_fingers_splayed:'},
    3: {'name': 'Tesoura', 'emoji': ':victory_hand:'}
}

player_score = 0
computer_score = 0

play_again = "S"

while play_again.lower() == "s":
    computer_choice = choice(list(options.keys()))
    print('Jokenpo vs Computador')
    print(emojize(f'''Faça a sua escolha:
        [1] {options[1]['name']} {options[1]['emoji']}
        [2] {options[2]['name']} {options[2]['emoji']}
        [3] {options[3]['name']} {options[3]['emoji']}'''))
    player_choice = int(input('Sua opção: '))
    while player_choice not in options.keys():
        player_choice = int(
            input('Digite um valor válido [1, 2 ou 3]. Qual é a sua jogada? '))

    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    sleep(1)

    print(emojize(
        f'O computador escolheu {options[computer_choice]["name"]} {options[computer_choice]["emoji"]}'))

    if player_choice == computer_choice:
        print(emojize(
            f'Você escolheu {options[player_choice]["name"]} {options[player_choice]["emoji"]}\n\033[1m\033[33mEMPATE\033[0m'))
    elif player_choice == 1 and computer_choice == 2 or player_choice == 2 and computer_choice == 3 or player_choice == 3 and computer_choice == 1:
        print(emojize(
            f'Você escolheu {options[player_choice]["name"]} {options[player_choice]["emoji"]}\n\033[1m\033[32mVOCÊ VENCEU\033[0m'))
        player_score += 1
    else:
        print(emojize(
            f'Você escolheu {options[player_choice]["name"]} {options[player_choice]["emoji"]}\n\033[1m\033[31mCOMPUTADOR VENCE\033[0m'))
        computer_score += 1

    play_again = input("Deseja jogar novamente? (S/N)").upper().strip()
    while play_again not in "SN":
        play_again = input(
            'Digite "S" para jogar novamente ou "N" para sair: ').upper().strip()

print(
    f'\nFim de jogo!\nPlacar final:\nVocê \033[1m\033[32m{player_score}\033[0m\033[0m x \033[1m\033[31m{computer_score}\033[0m\033[0m Computador')
