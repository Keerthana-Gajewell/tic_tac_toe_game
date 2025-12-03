import random

def print_board(board):
    print("\n")
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
    print("\n")

def check_winner(board, player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any(board[a] == board[b] == board[c] == player for a,b,c in win_conditions)

def tic_tac_toe():
    board = [" "] * 9
    user = "X"
    comp = "O"

    print("\n--- Tic-Tac-Toe ---")
    print_board(board)

    for turn in range(9):
        if turn % 2 == 0:
            while True:
                try:
                    move = int(input("Choose position (1-9): ")) - 1
                    if board[move] == " ":
                        board[move] = user
                        break
                    else:
                        print("Spot taken. Choose again.")
                except:
                    print("Invalid input.")
        else:
            print("Computer choosing...")
            empty = [i for i,v in enumerate(board) if v == " "]
            move = random.choice(empty)
            board[move] = comp

        print_board(board)

        if check_winner(board, user):
            print("🎉 You Win!")
            return
        if check_winner(board, comp):
            print("💻 Computer Wins!")
            return

    print("🤝 Match Draw!")
