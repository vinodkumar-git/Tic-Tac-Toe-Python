import itertools

def win(current_game):
    #for ROW WINNER
    for row in game:
        if row.count(row[0]) == len(row) and row[0] != 0:   #taking row[0] = 1/2 and having count of it
            print(f"Player {row[0]} is the Winner Horizontally (__) !")
            return True

    # for COLUMN WINNER
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != 0:  # taking row[0] = 1/2 and having count of it
            print(f"Player {row[0]} is the Winner Vertically ( | ) !")
            return True

    #left to right diagonal
    diags = []
    for index in range(len(game)):
        diags.append(game[index][index])  #appends [0,0] [1,1] and [2,2]
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:  # taking row[0] = 1/2 and having count of it
            print(f"Player {diags[0]} is the Winner Diagonally (\\) !")
            return True

    #right to left diagonal
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):      #enumerate prints the value with a counter ie., col is the counter
        diags.append(game[row][col])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:  # taking row[0] = 1/2 and having count of it
            print(f"Player {diags[0]} is the Winner Diagonally (/) !")
            return True
    return False

def game_board(game_map, player = 0, row = 0, column = 0, just_display = False):
    try:
        if game_map[row][column] != 0:
            print("This position is already Occupied! Please try someother position.")
            return game_map, False
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][column] = player
        for i,row in enumerate(game):
            print(i, row)
        return game_map, True
    except IndexError as e:
        print("Error: Are you sure you have input row/column as 0, 1 or 2!", e)
        return game_map, False
    except Exception as e:
        print("There must be something wrong!!", e)
        return game_map, False

players = [1,2]
play = True
while play:
    print("Hello welcome to TIC TAC TOE..")
    game_size = int(input("Please Enter the game size you want to play: "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle(players)
    game_won = False
    while not game_won:  # not True = false  or not is a false
        current_player = next(player_choice)
        print(f"current player : {current_player}")
        played = False
        while not played:
            column_choice = int(input("what column do u want to play? (0,1,2):"))
            row_choice = int(input("what row do u want to play? (0,1,2):"))
            game, played = game_board(game, current_player, row_choice, column_choice)   # if false is returned to played, while not played loops back again
        game_won = win(game)
        if game_won == True:
            again = input("The game is over... would u like to play again? (y/n): ")
            if again.lower() == "y":
                print("restarting .....")
            else:
                print("you dint select Yes... so Byeeee!!!")
                play = False





