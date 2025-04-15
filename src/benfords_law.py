import os
from pathlib import Path

# Benford's Law
script_dir = Path(__file__).parent
project_root = script_dir.parent

print("Files: ", os.listdir(f"{project_root}/data/benfords-law"))
file = input("file name: ")

raw_text_file = (
    open(f"{project_root}/data/benfords-law/{file}", "r").read().split("\n" or " ")
)

sum_of_numbers = 0
number_of_first_digits = [0, 0, 0, 0, 0, 0, 0, 0, 0]
benfords_law_percentile = [
    0.331,
    0.176,
    0.125,
    0.097,
    0.079,
    0.067,
    0.058,
    0.051,
    0.046,
]

print(raw_text_file)
for i in range(len(raw_text_file)):
    new_number = True
    for j in range(len(raw_text_file[i])):
        if new_number == True and 48 < ord(raw_text_file[i][j]) < 58:
            number_of_first_digits[int(raw_text_file[i][j]) - 1] += 1
            sum_of_numbers += 1
            new_number = False
        elif (
            new_number == False
            and ord(raw_text_file[i][j]) != 44
            and ord(raw_text_file[i][j]) != 46
            and 48 > ord(raw_text_file[i][j])
            or ord(raw_text_file[i][j]) > 58
        ):
            new_number = True

print(number_of_first_digits)
print(sum_of_numbers, "\n")

print("  \t ideal \t\t actual")
for i in range(len(number_of_first_digits)):
    print(
        f"{i + 1} \t {benfords_law_percentile[i]}\t\t {round(number_of_first_digits[i] / sum_of_numbers, 3)}\t"
    )
