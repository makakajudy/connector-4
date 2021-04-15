# project #1:Connect 4 game


def draw_field(field):
    # for the rows
    for row in range(13):
        real_row = int(row / 2)
        if row % 2 == 0:
            for col in range(13):
                if col % 2 == 0:
                    real_col = int(col / 2)
                    if col != 12:  # last column is col[12]
                        print(field[real_col][real_row], end=" ")
                    else:
                        print(field[real_col][real_row])
                else:
                    print("\u001b[33m|\u001b[0m", end=" ")
        else:
            print("\u001b[33m----------\u001b[0m" * 2)


def auto_row(row_list):
    pos = 0
    i = 0
    while i != len(row_list):  # while i is not = to size of list
        if row_list[i] != "":  # if value at a i is not empty/IS FILLED
            pos = i - 1  # set the pos to the previous pos
            break
        i += 1
    pos = i - (len(row_list) + 1)  # sets pos to last empty spot of almost filled row

    if pos == 0:
        pos = len(row_list) - 1  # if the whole row is empty pos is set to the last position.

    return pos


def returnWinner(field):
    for rrow in field:
        if len(set(rrow)) == 1:
            return rrow[0]
    return -1


# create a current_field list to keep track of the moves on the current field
current_field = [["", "", "", "", "", "", ""],  # list of row inside list of col. column1 row_pos 1-7
                 ["", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", ""]]
player = 1
draw_field(current_field)
game_loop = 0

while True:
    print(f'it is player {player}"s turn to play')
    move_col = int(input("\u001b[35m please select a column (0-6) to drop you piece in :\u001b[0m"))
    listOf_row = current_field[move_col]
    row_pos = auto_row(listOf_row)
    if player == 1:
        current_field[move_col][row_pos] = "\u001b[31m X \u001b[0m"
        returnWinner(current_field)

        player = 2

    else:
        current_field[move_col][row_pos] = "\u001b[36m O \u001b[0m"
        returnWinner(current_field)

        player = 1

    draw_field(current_field)

   # returnWinner(current_field)

    game_loop += 1
