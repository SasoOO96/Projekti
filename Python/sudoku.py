def valid_sudoku(board):
    # Provera redova
    for row in board:
        if not valid_set(row):
            return False

    # Provera kolona
    for col in zip(*board):
        if not valid_set(col):
            return False

    # Provera kvadrata dimenzija 3x3
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not valid_set(square):
                return False

    return True

def valid_set(nums):
    seen = set()
    for num in nums:
        if num != 0 and num in seen:
            return False
        seen.add(num)
    return True

def input_board():
    board = []
    for i in range(9):
        row = list(map(int, input(f"Unesite brojeve za red {i+1} (odvojene razmacima): ").strip().split()))
        board.append(row)
    return board

def print_board(board):
    for row in board:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    print("Unesite brojeve za Sudoku tablu (od 1 do 9):")
    sudoku_board = input_board()

    if valid_sudoku(sudoku_board):
        print("Uneta tabla je validan Sudoku.")
    else:
        print("Uneta tabla nije validan Sudoku.")
