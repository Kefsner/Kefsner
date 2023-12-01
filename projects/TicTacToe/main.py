import os

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
game_is_on = True


def can_draw(a, b):
    return board[a][b] == " "


def has_winner():
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board [1][1] == board[2][0] != ' ':
        return True
    if board[0][0] == board[0][1] == board[0][2] != ' ':
        return True
    if board[1][0] == board[1][1] == board[1][2] != ' ':
        return True
    if board[2][0] == board[2][1] == board[2][2] != ' ':
        return True
    if board[0][0] == board[1][0] == board[2][0] != ' ':
        return True
    if board[0][1] == board[1][1] == board[2][1] != ' ':
        return True
    if board[0][2] == board[1][2] == board[2][2] != ' ':
        return True
    return False


def draw(a, b, p):
    board[a][b] = p


def print_board():
    os.system('clear')
    for i in range(0, 3):
        print(board[i])


while game_is_on:
    player = 'x'

    while player == 'x':
        pos = input('Choose a coordinate for x: ')
        x, y = int(pos.split()[0]), int(pos.split()[1])

        if can_draw(x, y):
            draw(x, y, player)
            player = 'o'
        else:
            print("Wrong input!")

    print_board()

    if has_winner():
        print("The winner is x!")
        break

    while player == 'o':
        pos = input('Choose a coordinate for o: ')
        x, y = int(pos.split()[0]), int(pos.split()[1])

        if can_draw(x, y):
            draw(x, y, player)
            player = 'x'
        else:
            print("Wrong input!")

    print_board()

    if has_winner():
        print("The winner is o!")
        break
