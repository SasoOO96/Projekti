import random
free_list= [1,2,3,4,5,6,7,8,9]
def print_board(board):
    print("+-----+-----+-----+")
    print("|     |     |     |")
    print("|  " +board[1] + "  |  " + board[2] + "  |  " + board[3] + "  |")
    print("|     |     |     |")
    print("+-----+-----+-----+")
    print("|     |     |     |")
    print("|  " +board[4] + "  |  " + board[5] + "  |  " + board[6] + "  |")
    print("|     |     |     |")
    print("+-----+-----+-----+")
    print("|     |     |     |")
    print("|  " +board[7] + "  |  " + board[8] + "  |  " + board[9] + "  |")
    print("|     |     |     |")
    print("+-----+-----+-----+")

def check_winner(board):
    # Check rows
    for i in range(1, 8, 3):
        if board[i] == board[i+1] == board[i+2]:
            return board[i]

    # Check columns
    for i in range(1, 4):
        if board[i] == board[i+3] == board[i+6]:
            return board[i]

    # Check diagonals
    if board[1] == board[5] == board[9]:
        return board[1]
    if board[3] == board[5] == board[7]:
        return board[3]

    # Check for tie
    if len(free_list) == 0:
        return 'tie'

    # Game continues
    return None

def computer_move(board):
    while True:
        move = random.choice(free_list)
        if int(board[move]) in free_list:
            free_list.remove(move)
            return move

def main():
    
    board = {i: str(i)for i in free_list}
    
    print("Welcome to Tic-Tac-Toe!")

    # Computer places its first move
    tmp= random.choice(free_list)
    board[tmp] = 'X'
    free_list.remove(tmp)
    
    print_board(board)

    while True:
        # Player's move
        while True:
            user_move = int(input("Enter your move (1-9): "))
            if user_move not in free_list:
                print("Invalid move. Please try again.")
            elif int(board[user_move]) in free_list:
                free_list.remove(user_move)
                board[user_move] = 'O'
                break
            else:
                print("Invalid move. Please try again.")
        print_board(board)

        # Check if user wins or tie
        winner = check_winner(board)
        if winner == 'O':
            print("Congratulations! You win!")
            break
        elif winner == 'tie':
            print("It's a tie!")
            break

        # Computer's move
        comp_move = computer_move(board)
        board[comp_move] = 'X'
        print("Computer's move:", comp_move)
        print_board(board)

        # Check if computer wins or tie
        winner = check_winner(board)
        if winner == 'X':
            print("Computer wins!")
            break
        elif winner == 'tie':
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
