import sys


def tricky_game_winner(N, player_1_list, player_2_list):
    player1_point = 0
    player2_point = 0

    for i in range(N):
        if player_1_list[i] > player_2_list[i]:
            player1_point += 1
        elif player_1_list[i] < player_2_list[i]:
            player2_point += 1

    if player1_point > player2_point:
        print('PLAYER 1 WINS')
    elif player1_point < player2_point:
        print('PLAYER 2 WINS')
    else:
        print('TIE')


def main():
    contents = sys.stdin.readlines()

    N = int(contents[0])


    # obtain the card list played by player 1
    player_1_list = []
    for i in contents[1].rstrip('\n').split(' '):
        if i == 'J':
            player_1_list.append(10)
        elif i == 'Q':
            player_1_list.append(11)
        elif i == 'K':
            player_1_list.append(12)
        elif i == 'A':
            player_1_list.append(13)
        else:
            player_1_list.append(int(i))

    # obtain the card list played by player 2
    player_2_list = []
    for i in contents[2].rstrip('\n').split(' '):
        if i == 'J':
            player_2_list.append(10)
        elif i == 'Q':
            player_2_list.append(11)
        elif i == 'K':
            player_2_list.append(12)
        elif i == 'A':
            player_2_list.append(13)
        else:
            player_2_list.append(int(i))

    tricky_game_winner(N, player_1_list, player_2_list)


if __name__ == '__main__':
    main()

