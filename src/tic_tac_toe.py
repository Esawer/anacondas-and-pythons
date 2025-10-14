from copy import deepcopy
from pathlib import Path

dir_path = Path(__file__).parent


def game_history(player_one: bool, tie: bool, flattened_field):
    try:
        game_stats = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}  # {"O wins": 0, "X wins": 0, "Ties": 0, "O moves": 0, "X moves": 0}
        game_stats_text = ("⭕ wins: ", "❌ wins: ", "🤝 Ties: ", "🟠 moves: ", "❎ moves: ", "🌍 Total moves: ")

        with open(f"{dir_path}\\game_stats.txt", "r") as f:
            for i in range(len(game_stats)):
                game_stats[i] = f.readline().strip()

        if tie:
            game_stats[2] = str(int(game_stats[2]) + 1)
        elif player_one:
            game_stats[0] = str(int(game_stats[0]) + 1)
        else:
            game_stats[1] = str(int(game_stats[1]) + 1)

        game_stats[3] = str(int(game_stats[3]) + int(len([a for a in flattened_field if a == "O"])))
        game_stats[4] = str(int(game_stats[4]) + int(len([a for a in flattened_field if a == "X"])))

        print("\nGAMES HISTORY")
        for i in range(len(game_stats)):
            print(f"{game_stats_text[i]} {game_stats[i]}")
        print(game_stats_text[-1], int(game_stats[3]) + int(game_stats[4]))

        with open(f"{dir_path}\\game_stats.txt", "w") as f:
            for i in game_stats.values():
                f.write(f"{i}\n")

    except (FileNotFoundError, TypeError, ValueError):
        with open(f"{dir_path}\\game_stats.txt", "w") as f:
            for i in range(5):
                f.write(f"0\n")


def field_show(field: list, field_size):
    """
    Function responsible for showing the field of game, according to the field_size parameter(provided by the user)
    :param field: the field of the game itself, with real-time player positions
    :param field_size: size of this field
    TO-CHECK: if it is better to use var field_size over the len(field).
    :return:
    """
    for i in range(field_size):
        if i == 0: print("\t", "".join([f"  {k + 1}\t " for k in range(field_size)]))

        print("\t_______" * field_size)
        for j in range(field_size):
            if j == 0: print(chr(65 + i), end="\t")
            print(f" {"|" if j == field_size else "|"} {field[i][j]} {"|" if j != field_size - 1 else "|"}", end="\t")
        print()
    else:
        print("\t_______" * field_size)


def game_end(player_one: bool, custom_mode: bool, field: list, tie: bool = False):
    flattened_field = []
    for i in field:
        for j in i:
            flattened_field.append(j)

    if tie:
        print(f"\n⭕TIE❌")
    else:
        print(f"\nHurray, {"O" if player_one else "X"} has won!")
    print("_______STATS_______")
    print(f"{"STANDARD MODE" if custom_mode == False else "CUSTOM MODE"}\n"
          f"TOTAL MOVES: {len([a for a in flattened_field if a != " "])}\n"
          f"⭕ MOVES: {len([a for a in flattened_field if a == "O"])}\n"
          f"❌ MOVES: {len([a for a in flattened_field if a == "X"])}")

    game_history(player_one, tie, flattened_field)

    main_menu() if input("\n# Would you like to play again(y/n):\n> ").strip().lower() in ('y', 'yes', '1') else (print(
        "Thank you for playing!"), exit())


def point_win_checker(check_value: list, points: int):
    player_points = 0
    player_char = ""

    for i, j in enumerate(check_value):
        if j == " ":
            continue
        else:
            if player_char == j:
                player_points += 1
            else:
                player_char = j
                player_points = 1

            if player_points >= points:
                return True

    return False


def pre_win_checker(field: list, custom_mode: bool, position):
    """
    standard field to check for horizontal win
    deepcopy of standard rotated in such way that we can use it as horizontal
    then:
    we take 00 11 22; 10 22; 01 21; 20 11 02 etc. and check for diagonally
    x o x
    o x x
    x x o
    """
    b = deepcopy(field)
    c = []
    d = []
    row = ord(position[0]) - 65
    col = int(position[1]) - 1
    points = 3

    for i in range(len(field)):
        for j in range(len(field)):
            b[i][j] = field[j][i]

    while True:
        row_checker = row
        col_checker = col

        while True:
            if row_checker > 0 and col_checker > 0:
                row_checker -= 1
                col_checker -= 1
            else:
                while True:
                    c.append(field[row_checker][col_checker])
                    if row_checker < len(field) - 1 and col_checker < len(field) - 1:
                        row_checker += 1
                        col_checker += 1
                    else:
                        break
                """print(([a[row_checker+i][col_checker+i] for i in range(min(len(a) - row_checker, len(a) - col_checker))]))"""
                row_checker = row
                col_checker = col
                break

        while True:
            if row_checker > 0 and col_checker < len(field) - 1:
                row_checker -= 1
                col_checker += 1
            else:
                while True:
                    d.append(field[row_checker][col_checker])
                    if row_checker < len(field) - 1 and col_checker > 0:
                        row_checker += 1
                        col_checker -= 1
                    else:
                        break

                """r_s = row_checker
                c_s = col_checker
                print(([a[row_checker+i][col_checker-i] for i in range(min(len(a) - r_s, 1 + c_s))]))"""
                break
        break

    """    print(([a for a in field[row]]))
    print(([a for a in b[col]]))
    print(c)
    print(d)"""

    if custom_mode:
        points = int(len(field))
        if points > 5:
            points -= 1

    for i in [[a for a in field[row]], [a for a in b[col]], c, d]:
        if point_win_checker(i, points):
            return True
    else:
        return False


def game_start(custom_mode: bool = False, field_size: int = 3):
    """
    Start of the game, players choose and field is shown.

    :param custom_mode: bool, is this custom mode(field_size=2-8) or standard mode (field size(3x3))
    :param field_size: by default it is 3, ergo standard mode, when in main_menu() the use chooses differently, this value also changes.
    :return:
    """
    field = [[" " for _ in range(field_size)] for _ in range(field_size)]
    player_1_turn = True
    game_running = True

    for i in range((field_size * field_size) + 1):
        field_show(field, field_size)

        if i == field_size * field_size:
            game_running = False
            game_end(player_1_turn, custom_mode, field, True)

        while game_running:
            try:
                position = input(f"{"Player O" if player_1_turn else "Player X"}, choose(eg.A1):\n> ").upper().strip()
                if len(position) == 2 and (64 < ord(position[0]) < 91) and int(position[1]) <= field_size:
                    if field[ord(position[0]) - 65][int(position[1]) - 1] == " ":
                        field[ord(position[0]) - 65][int(position[1]) - 1] = ("O" if player_1_turn else "X")
                        if pre_win_checker(field, custom_mode, position):
                            game_running = False
                            field_show(field, field_size)
                            game_end(player_1_turn, custom_mode, field, False)
                        player_1_turn = not player_1_turn
                        break
                    else:
                        raise ValueError
                else:
                    raise ValueError

            except (ValueError, IndexError, TypeError):
                print("Enter correct position.")


def main_menu():
    """
    Main menu, starts at the beginning of the program.
    :return:
    """
    running = True

    print("""
            -----------------
            ❌ TIC-TAC-TOE ⭕
            -----------------
            1. STANDARD MODE
            2. CUSTOM MODE
            3. EXIT
            """)

    while running:

        match input("> "):
            case "1":
                running = False
                game_start()
            case "2":
                while True:
                    try:
                        field_size = input("field size(2-8):\n#type b to go back\n> ").lower().strip()

                        if field_size == "b":
                            main_menu()

                        if 2 > int(field_size) or int(field_size) > 8:
                            raise ValueError
                        else:
                            running = False
                            game_start(True, int(field_size))

                    except (ValueError, TypeError):
                        print("Please enter correct value.\n")

            case "3":
                running = False
            case _:
                print("Please enter correct input.")


main_menu()
