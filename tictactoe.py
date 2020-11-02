# start function->1
def start():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    print("Welcome to tic tac toe!")
    display1_board()
    player1 = input("Select the char player1 X/O:")
    if (player1 != "X") and (player1 != "O"):
        print("Error in the selection of characters!")
        player1 = input("Select the char player1 X/O:")
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"
    print(f"Player2 character is:{player2}")
    display_board(board)
    game(player1, player2, board)


# display1_board->2
def display1_board():
    print("The position indices are:")
    print('7|8|9')
    print("- - -")
    print('4|5|6')
    print("- - -")
    print('1|2|3')


# game begins and ends->3
def game(player1, player2, board):
    w1 = 0
    w2 = 0
    w3 = 0
    while (w1 == 0) and (w2 == 0) and (w3 == 0):
        play1(player1, player2, board)
        w1 = check1(board, player1)
        if w1 == 1:
            break
        w3 = finalcheck(board)
        if w3 == 1:
            break
        play2(player2, player1, board)
        w2 = check2(board, player2)
        if w2 == 1:
            break
        w3 = finalcheck(board)
        if w3 == 1:
            break
    if w1 == 1:
        print("Player1 wins")
    elif w2 == 1:
        print("Player2 wins")
    elif w3 == 1:
        print("The match is a draw")
    s = input("Do you wish to play another game?(Y/N):")
    if s == "Y":
        start()
    else:
        print("Adios Amigos!")


# player1 input->4
def play1(player1, player2, board):
    player1pos = int(input("Enter the positions for the char player1:"))
    li = list(range(1, 10))
    if player1pos not in li:
        print("Select a correct index")
        player1pos = int(input("Enter the positions for the char player1:"))
    if board[player1pos - 1] == player2:
        print("Error player2 has already place there")
        play1(player1, player2, board)
    else:
        board[player1pos - 1] = player1
        display_board(board)


# player2 input->4
def play2(player2, player1, board):
    player2pos = int(input("Enter the position player2:"))
    li = list(range(1, 10))
    if player2pos not in li:
        print("Select a correct index!")
        player2pos = int(input("Enter the position player2:"))
    if board[player2pos - 1] == player1:
        print("Error player1 has already place there")
        play2(player2, player1, board)
    else:
        board[player2pos - 1] = player2
        display_board(board)


# display_board->6
def display_board(board):
    print(f'{board[6]}|{board[7]}|{board[8]}')
    print("- - -")
    print(f'{board[3]}|{board[4]}|{board[5]}')
    print("- - -")
    print(f'{board[0]}|{board[1]}|{board[2]}')


# for player1 check->6
def check1(board, player1):
    if board[0] == board[1] == board[2] == player1:
        return 1
    elif board[0] == board[4] == board[8] == player1:
        return 1
    elif board[1] == board[4] == board[7] == player1:
        return 1
    elif board[2] == board[5] == board[8] == player1:
        return 1
    elif board[2] == board[4] == board[6] == player1:
        return 1
    elif board[3] == board[4] == board[5] == player1:
        return 1
    elif board[6] == board[7] == board[8] == player1:
        return 1
    elif board[0] == board[3] == board[6] == player1:
        return 1
    else:
        return 0


# for player2 check->6
def check2(board, player2):
    if board[0] == board[1] == board[2] == player2:
        return 1
    elif board[0] == board[4] == board[8] == player2:
        return 1
    elif board[1] == board[4] == board[7] == player2:
        return 1
    elif board[2] == board[5] == board[8] == player2:
        return 1
    elif board[2] == board[4] == board[6] == player2:
        return 1
    elif board[3] == board[4] == board[5] == player2:
        return 1
    elif board[6] == board[7] == board[8] == player2:
        return 1
    elif board[0] == board[3] == board[6] == player2:
        return 1
    else:
        return 0


# final check for draw->7
def finalcheck(board):
    if " " not in board:
        return 1
    else:
        return 0


start()
