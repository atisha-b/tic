def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False

    while not game_over:
        print_board(board)
        print(f"Player {current_player}'s turn:")
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                game_over = True
            elif all(cell != " " for row in board for cell in row):
                print_board(board)
                print("It's a tie!")
                game_over = True
            else:
                current_player = "X" if current_player == "O" else "O"
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    main()
