import os
import random
from pathlib import Path

script_dir = Path(__file__).parent
project_root = script_dir.parent
data_files = os.listdir(f"{project_root}/data/benfords-law")

print("Files: ")
for i in range(len(data_files)):
    print(f"{i}. {data_files[i]}")

file = int(input("\nfile number: "))

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

with open(f"{project_root}/data/benfords-law/{data_files[file]}", "r") as read_file:
    raw_text_file = read_file.read().split("\n" or " ")

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

if sum_of_numbers == 0:
    sum_of_numbers = 1
output_name = f"{data_files[file]}_output"

with open(
    f"{project_root}/output/benfords_law_output/{output_name}", "w"
) as output_file:
    output_file.writelines("  \t ideal \t\t actual\n")
    for i in range(len(number_of_first_digits)):
        output_file.writelines(
            f"{i + 1} \t {benfords_law_percentile[i]}\t\t {round(number_of_first_digits[i] / sum_of_numbers, 3)}\t\n"
        )
