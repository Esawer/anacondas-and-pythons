"""
pathlib

Time counter for english and spanish study
as well as for programming!

1. choose between programming and language file
2. CLI menu with options (above in menu)
3. add, change, view, stats, progress/milesones
4. create new file(?)
5. gui and flask(future)

"""

milestones = {
    "0": 0,
    "1": 25,
    "2": 50,
    "3": 150,
    "4": 300,
    "5": 600,
    "6": 1000,
    "7": 1500,
    "8": 1800,
    "9": 2000,
    "10": 2500
}

file_structure = []
top_row = ""

def file_add():
    record = "\n"
    with open("C:\\Users\\igore\\PycharmProjects\\anacondas-and-pythons\\data\\time-counter-data\\language", 'a') as fa:
        record += str(int(file_structure[-1][0]) + 1) + ","
        record += input("\n# Date(dd/mm/yyyy)\n> ") + ","
        record += input("\n# Time(in min)\n> ") + ","
        record += input("\n# Description\n> ")

        fa.writelines(record) if input(f"# {record.replace(',', ' ').replace('\n',"")}, do you wish to discard it(y/n)\n> ").lower() == 'n' else ""
        file_menu(True)

def file_show(show_stats_or_log: bool, minutes, level, next_level):
    global top_row

    if show_stats_or_log:
        print(top_row.replace(',', '\t'))
        for i in range(len(file_structure)):
            print(file_structure[i][0], "\t", file_structure[i][1], "\t", file_structure[i][2], "\t", file_structure[i][3])
    else:
        print(f"""
        # Time in language #
        # in minutes: {minutes}min
        # in hours: {minutes / 60}h
        # level: Level {level}
        # next level in: {(milestones[next_level] - (minutes / 60)):.2f}h
        """)

    input("\n# Input anything to go back.\n> ")
    file_menu(True)


def file_menu(open_file: bool):
    global top_row
    minutes = 0
    level = 0
    next_level = 0
    file_menu_choice = True

    if open_file:
        with open("C:\\Users\\igore\\PycharmProjects\\anacondas-and-pythons\\data\\time-counter-data\\language", 'r') as f:
            top_row = f.readline()
            for line in f:
                file_structure.append(line.split(','))
                minutes += int(file_structure[-1][2] or 0)

    for i, j in milestones.items():
        if minutes / 60 >= j:
            level = i
        else:
            next_level = i
            break

    print("""
        ####################
        # 1. ADD RECORD    #
        # 2. SHOW STATS    #
        # 3. SHOW LOG      #
        # 4. GO BACK       #
        ####################""")

    while file_menu_choice:

        match input("> "):
            case "1":
                file_add()
            case "2":
                file_show(False, minutes, level, next_level)
            case "3":
                file_show(True, minutes, level, next_level)
            case "4":
                file_menu_choice = not file_menu_choice
            case _:
                print("Wrong Input")


def main_menu(menu_choice: bool = True):

    print("""
    ####################
    # 1. OPEN FILE     #
    # 2. CREATE FILE   #
    # 2. EXIT PROGRAM  #
    ####################""")

    while menu_choice:

        match input("> "):
            case "1":
                file_menu(True)
                main_menu()
            case "2":
                file_menu(False)
                main_menu()
            case "3":
                menu_choice = not menu_choice
            case _:
                print("Wrong Input")


main_menu()
