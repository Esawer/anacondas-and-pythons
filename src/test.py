# level 3.5(1st); 5.3(1st)?
# zip and loop unpacking exer
# str.maketrans(); .format
# pathlib

import json
import os
import random


def game_start(game_questions):
    points = 0
    supporting_list = ["a", "b", "c", "d", "e"]

    for i in range(len(game_questions["questions"])):
        print(f"{i + 1}. {game_questions["questions"][i]["question"]}",
              f"\tdifficulty - {game_questions["questions"][i]["difficulty"]}")

        questions_ans = game_questions["questions"][i]["answers"]
        random.shuffle(questions_ans)

        for j in range(len(questions_ans)):
            print(f" {supporting_list[j]})", game_questions["questions"][i]["answers"][j])

        while True:
            u_input = input("\n> ").lower()

            if u_input in supporting_list:
                if game_questions["questions"][i]["correct"] == questions_ans[supporting_list.index(u_input)]:
                    points += 1
                    print("Correct!\n")
                else:
                    print("Incorrect.\n")
                break

            else:
                print("Wrong input")

    print(f"Your score: {points} / {len(game_questions["questions"])}",
          "- perfect score!" if points == len(game_questions["questions"]) else "")

    if input("\n# Would you like to play again(y/n)?\n> ").lower() == ("y", "1"):
        file_choose_menu()
    else:
        print("Thank you for playing.")


def file_choose_menu():
    data = 0

    while True:
        print("\nSELECT FILE:")

        try:
            game_files = os.listdir(r"C:\Users\igore\PycharmProjects\anacondas-and-pythons\data\test_data")
            if not game_files: raise FileNotFoundError

            for i, j in enumerate(game_files, 1):
                print(f"{i}. {j}")

            if 0 < (a := int(input("\n> "))) <= len(game_files):
                with open(fr"C:\Users\igore\PycharmProjects\anacondas-and-pythons\data\test_data\{game_files[a - 1]}",
                          "r") as f:
                    data = json.load(f)

                return data
            else:
                raise TypeError

        except FileNotFoundError:
            print("Error - no files found")
            return None

        except TypeError:
            print("Error - wrong input value")

        except ValueError:
            print("Error - wrong input type")


def main_menu():
    running = True

    (print
     (""" 
    % QUIZ GAME %
    1. START GAME
    2. CREATOR
    3. EXIT GAME
    """))

    while running:

        match input("> "):
            case "1":
                file_dat = file_choose_menu()
                if file_dat is not None:
                    game_start(file_dat)
                running = False
            case "2":
                print(f"CREATOR----> Esawer\n")
            case "3":
                running = False
            case _:
                print("Enter correct input.")

main_menu()