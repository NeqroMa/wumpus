from random import randrange

"""
2D Wumpus Game

movement keys: w, a, s, d
vitory: collect all loot
game over: touch wumpus
quit key: q

"""

# initialize variables necessary for the game to run
playing_field = []
loot_field = []
field_size = 10
num_of_loot = 5


# initializes the game field
def initialize_game(playing_field):
    for i in range(field_size):
        row = []
        for j in range(field_size):
            row.append(0)
        playing_field.append(row)
    return()

# displays the playing field
def display_map():
    len_field = len(playing_field)
    for pos_row in range(len_field):
        for pos_col in range(len_field):
            if playing_field[pos_row][pos_col] == 0:
                print('. ', end="")
            if playing_field[pos_row][pos_col] == 1:
                print('@ ', end="")
            if playing_field[pos_row][pos_col] == 2:
                print('$ ', end="")
            if playing_field[pos_row][pos_col] == 3:
                print('W ', end="")
        print()
    print()
    return()

# makes a copy of the current position before movement
def old_pos():
    old_player_pos = []
    for i in range(len(player_pos)):
        old_player_pos.append(player_pos[i])
    return(old_player_pos)

# places loot on the map in a different position than the player and stores
# position value in a loot_field (list)
def place_loot(playing_field, num_of_loot):
    for i in range(num_of_loot):
        row, col = randrange(0, field_size), randrange(0, field_size)
        if row != player_pos[0] or col != player_pos[1]:
            playing_field[row][col] = 2
            loot_field.append([row,col])
    return()


def place_wumpus():
    placed_wumpus = False
    row, col = randrange(0, field_size), randrange(0, field_size)
    while place_wumpus == False:
        if row != player_pos[0] or col != player_pos[1]:
            checker = 0
            for i in range(num_of_loot):
                if loot_field[i][0] == row and loot_field[i][1] == col:
                    checker += 1
            if checker != 0:
                row, col = randrange(0, field_size), randrange(0, field_size)
                break

        placed_wumpus = True

    wumpus_pos = [row,col]
    playing_field[row][col] = 3
    return(wumpus_pos)

# checks if loot is collected
def check_loot(num_of_loot):
    for i in range(num_of_loot):
        if loot_field[i][0] == player_pos[0] and loot_field[i][1] == player_pos[1]:
            num_of_loot -= 1
            loot_field.remove(loot_field[i])
            return(num_of_loot)
    return(num_of_loot)

# def check_wumpus():
#     if

# initialize the game, set player positoin, loot, and wumpus
initialize_game(playing_field)

player_pos = [randrange(0, field_size),randrange(0, field_size)]
playing_field[player_pos[0]][player_pos[1]] = 1

place_loot(playing_field, num_of_loot)
wumpus_pos = place_wumpus()

# display game and provide controls
display_map()

print("(w) - up")
print("(a) - left")
print("(s) - down")
print("(d) - right")
print("(q) - quit")
movement_command = input("Enter your command: ")

if movement_command == 'q':
    keep_playing = False
else:
    keep_playing = True



while keep_playing == True:
    num_of_loot = check_loot(num_of_loot)
    if num_of_loot == 0:
        keep_playing = False

    elif movement_command == 'q':
        keep_playing = False

    elif wumpus_pos[0] == player_pos[0] and wumpus_pos[1] == player_pos[1]:
        playing_field[player_pos[0]][player_pos[1]] = 3
        keep_playing = False

    else:
        if movement_command == 'a':
            old_player_pos = old_pos()
            player_pos[1] -= 1

            if player_pos[1] < 0:
                player_pos[1] = field_size - 1

            playing_field[player_pos[0]][player_pos[1]] = 1
            playing_field[old_player_pos[0]][old_player_pos[1]] = 0

        elif movement_command == 'd':
            old_player_pos = old_pos()
            player_pos[1] += 1

            if player_pos[1] > field_size - 1:
                player_pos[1] = 0

            playing_field[player_pos[0]][player_pos[1]] = 1
            playing_field[old_player_pos[0]][old_player_pos[1]] = 0

        elif movement_command == 'w':
            old_player_pos = old_pos()
            player_pos[0] -= 1

            if player_pos[0] < 0:
                player_pos[0] = field_size - 1

            playing_field[player_pos[0]][player_pos[1]] = 1
            playing_field[old_player_pos[0]][old_player_pos[1]] = 0

        elif movement_command == 's':
            old_player_pos = old_pos()
            player_pos[0] += 1

            if player_pos[0] > field_size - 1:
                player_pos[0] = 0

            playing_field[player_pos[0]][player_pos[1]] = 1
            playing_field[old_player_pos[0]][old_player_pos[1]] = 0





        display_map()
        movement_command = input("Enter your command: ")



if num_of_loot == 0:
    print("Victory! All loot collected!")
elif wumpus_pos[0] == player_pos[0] and wumpus_pos[1] == player_pos[1]:
    print("You are dead!")
else:
    print("Game Over")






#
