import random

target = random.randint(1, 100)

while True:
    player_input = input("Guess the number (1 - 100): ")
    if not player_input.isdigit():
        print("Invalid input, please try again")
        continue
    player_input = int(player_input)
    if player_input == target:
        print("YOU WIN!!!")
    elif player_input > target:
        print(f"The number is smaller than {player_input}")
    elif player_input < target:
        print(f"The number is bigger than {player_input}")
