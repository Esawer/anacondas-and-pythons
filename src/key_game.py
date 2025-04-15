import random


# key game - project 1, well working


def player_moving():
    while True:
        if found_the_key:
            return 0
        player_move = input(f"You are on square {player}, where do you wish to go: ")
        x = player[0]
        y = player[1]

        if (player_move == "w" or player_move == "W") and player[0] != 0:
            player[0] -= 1
            break
        elif (player_move == "a" or player_move == "A") and player[1] != 0:
            player[1] -= 1
            break
        elif (player_move == "d" or player_move == "D") and player[1] != map_size - 1:
            player[1] += 1
            break
        elif (player_move == "s" or player_move == "S") and player[0] != map_size - 1:
            player[0] += 1
            break
        else:
            continue


map_size = 0
player_moves = 0
while map_size <= 2:
    map_size = int(input("Map size: "))

game_map = [[0 for i in range(map_size)], [0 for i in range(map_size)]]
player = [random.randrange(0, map_size), random.randrange(0, map_size)]
key = player
found_the_key = False

while key == player:
    key = [random.randrange(0, map_size), random.randrange(0, map_size)]

while not found_the_key:
    for i in range(map_size):
        for j in range(map_size):
            if i != player[0] or j != player[1]:
                print("#", end=" ")
            elif key == player:
                found_the_key = True
                print("*", end=" ")
            elif i == player[0] or j == player[1]:
                print("@", end=" ")
        print("")
    print("")
    player_moving()
    player_moves += 1

print(
    f"Hurry, you have found the key at {player[1]},{player[0]} - using only {player_moves}!"
)
