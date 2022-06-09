# creating the project in python ( creating game of tic-tac-toe)

def dummy_display():
    print("0" + "  |  " + "1" + "  |  " + "2")
    print("3" + "  |  " + "4" + "  |  " + "5")
    print("6" + "  |  " + "7" + "  |  " + "8")


def display(row1, row2, row3):
    print(row1[0] + "  |  " + row1[1] + "  |  " + row1[2])
    print(row2[0] + "  |  " + row2[1] + "  |  " + row2[2])
    print(row3[0] + "  |  " + row3[1] + "  |  " + row3[2])
    print()


def win_check(row1, row2, row3, Mark):
    if ((row1[0] == row1[1] == row1[2] == Mark) or
            (row2[0] == row2[1] == row2[2] == Mark) or
            (row3[0] == row3[1] == row3[2] == Mark) or
            (row1[0] == row2[0] == row3[0] == Mark) or
            (row1[1] == row2[1] == row3[1] == Mark) or
            (row1[2] == row2[2] == row3[2] == Mark) or
            (row1[0] == row2[1] == row3[2] == Mark) or
            (row1[2] == row1[1] == row1[0] == Mark)):

        return False

    else:
        return True


def draw_game(row1, row2, row3):
    if ((row1[0] == row1[1] == row1[2] == " ") and
            (row2[0] == row2[1] == row2[2] == " ") and
            (row3[0] == row3[1] == row3[2] == " ")):

        return True

    else:
        return False


dummy_display()
row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

Mark = [" ", " "]

game_on = True
choosing = True
Player_num = 1

while game_on:

    cur_input = True

    while choosing:

        sign = int(input("Player " + str(Player_num) + " Choose your Mark Enter 1 for 'O' or 2 for 'X'\n"))
        if sign == 1 or sign == 2:
            choosing = False
        else:
            print("You have entered wrong number Try again")

    if sign == 1:
        Mark[0] = "O"
        Mark[1] = "X"
    else:
        Mark[0] = "X"
        Mark[1] = "O"

    while cur_input:
        choice = int(input("Player " + str(Player_num) + " Enter number of your choice(1-9)\n"))
        if choice not in range(0, 9):
            print("You have entered wrong input")
        else:
            cur_input = False

    if choice < 3:
        row1[choice] = Mark[Player_num - 1]

    elif 2 < choice < 6:
        row2[choice - 3] = Mark[Player_num - 1]

    else:
        row3[choice - 6] = Mark[Player_num - 1]

    display(row1, row2, row3)

    game_on = win_check(row1, row2, row3, Mark[Player_num - 1])

    if game_on is False:
        print("Player " + str(Player_num) + " has Won the game")

    if draw_game(row1, row2, row3):
        print("There has been a tie")
        exit()

    if Player_num == 1:
        Player_num = 2
    else:
        Player_num = 1

    if game_on is False:
        print("Do you want to play again")
        again = int(input("Press 1 for YES and 2 for NO"))
        if again == 1:
            row1 = [" ", " ", " "]
            row2 = [" ", " ", " "]
            row3 = [" ", " ", " "]

            Mark = [" ", " "]

            game_on = True
            choosing = True
            Player_num = 1
        else:
            exit()
