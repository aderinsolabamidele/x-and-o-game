
Tic-Tac-Toe is a classic paper-and-pencil game typically played by two players, often called X and O, who take turns marking the spaces in a 3x3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game. If all spaces are filled without either player achieving this, the game ends in a draw.

To create the Tic-Tac-Toe game in Python, I utilized a few key concepts:

Data Representation: I used a 2-dimensional list (board) to represent the game board. Each element of the list represents a space on the board, initially filled with empty strings to denote unmarked spaces.

Printing the Board: The print_board() function is used to display the current state of the game board on the console.

Game Logic: The check_winner() function determines whether there is a winner by checking the rows, columns, and diagonals of the board to see if any player has placed three marks in a row.

Main Game Loop: The tic_tac_toe() function controls the flow of the game. It repeatedly prompts players for their moves, updates the board, checks for a winner or a tie, and alternates between players until the game ends.

Input Validation: I included basic input validation to ensure that players enter valid row and column numbers for their moves. If a player attempts to choose a space that is already occupied, the program prompts them to choose another space.

By combining these elements, the Python code implements a basic but functional version of the Tic-Tac-Toe game that allows two players to play against each other on the console
