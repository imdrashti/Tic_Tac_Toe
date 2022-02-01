print("Tic Tac Toe")
print("Enter the relevant number for your symbol according to the board.\n")

grid = ['0', '1', '2',
        '3', '4', '5',
        '6', '7', '8']


def printBoard(board):
    print(board[0] + " " + board[1] + " " + board[2])
    print(board[3] + " " + board[4] + " " + board[5])
    print(board[6] + " " + board[7] + " " + board[8])


#printBoard(grid)

                                                    #return names of players
def player():
    player1 = input("Enter the name of Player X: ")
    player2 = input("Enter the name of Player O: ")
    return player1, player2

player()


def playerTurn():
    moves = []                                # to save the position numbers so that same number is not repeated
    move1 = int(input("Enter the position number for X: "))
    move2 = int(input("Enter the position number for O: "))


    grid[move1] = "X"
    moves.append(move1)

    grid[move2] = "O"
    moves.append(move2)
    printBoard(grid)
    print("Positions you cannot use: ", moves)


#playerTurn()

game_is_on = True

while game_is_on:
    printBoard(grid)
    playerTurn()

    if grid[0] == grid[1] == grid[2]:
        print(f"The winner is player {grid[1]}.")
        game_is_on = False
    elif grid[0] == grid[4] == grid[8]:
        print(f"The winner is player {grid[1]}.")
        game_is_on = False
    elif grid[0] == grid[3] == grid[6]:
        print(f"The winner is player {grid[1]}.")
        game_is_on = False
    elif grid[1] == grid[4] == grid[7]:
        print(f"The winner is player {grid[1]}.")
        game_is_on = False
    elif grid[2] == grid[5] == grid[8]:
        print(f"The winner is player {grid[1]}.")
        game_is_on = False
    elif grid[3] == grid[4] == grid[5]:
        print(f"The winner is player {grid[1]}.")
        game_is_on = False
    elif grid[6] == grid[7] == grid[8]:
        print(f"The winner is player {grid[1]}.")
        game_is_on = False
    elif grid[2] == grid[4] == grid[6]:
        print(f"The winner is player {grid[1]}.")
        game_is_on = False
    else:
        continue







