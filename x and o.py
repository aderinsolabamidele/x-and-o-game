def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] !=' ':
            return True
        
    for col in range(len(board[0])):
        if all(board[row][col]== board[0][col] and board[0][col] != ' ' for row in range(len(board))):
            return True
        
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    

    return False

def tic_tac_toe():
   board = [[" " for _ in range(3)] for _ in range(3)]
   current_player = "X"

   
   while True:
        
        print_board(board)
        print("It's player", current_player, "'s turn.")
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))

        if board[row][col] != " ":
            print("That position is already taken!")
            continue

        board[row][col] = current_player

        if check_winner(board):
            print_board(board)
            print("Player", current_player, "wins!")
            break

        if all(all(cell != " " for cell in row) for row in board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()