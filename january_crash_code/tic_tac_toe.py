# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if a player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Function to check if the board is full (draw)
def is_draw(board):
    return all(cell != " " for row in board for cell in row)

# Main game loop
def tic_tac_toe():
    print("Welcome to Tic Tac Toe!")
    board = [[" " for _ in range(3)] for _ in range(3)]  # 3x3 empty board
    players = ["X", "O"]
    turn = 0  # Tracks the current player's turn

    while True:
        print_board(board)
        player = players[turn]
        print(f"Player {player}'s turn.")

        # Input the player's move
        try:
            row, col = map(int, input("Enter your move (row and column, 0-2): ").split())
            if board[row][col] != " ":
                print("Cell already occupied! Try again.")
                continue
            board[row][col] = player
        except (ValueError, IndexError):
            print("Invalid input! Enter row and column as two numbers between 0 and 2.")
            continue

        # Check for win or draw
        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch turn to the other player
        turn = 1 - turn

# Run the game
tic_tac_toe()
