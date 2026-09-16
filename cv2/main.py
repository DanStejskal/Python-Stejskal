from random import random

def get_color():
    value = random * 100
    if value <= 3:
        return 2
    elif value <= 51.5:
        return 0
    else:
        return 1

def start_game():
    print("Welcome to casino royal")
    bet = int(input("Enter your bet: "))

    print(" Select color:")
    print("\t\t0 - Red")
    print("\t\t1 - Black")
    print("\t\t2 - Green")
    print("\t\t9 - Leave game")
    selection = int(input("Enter your choice: "))

    if selection == 9:
        print("Thanks for playing!")
        return

    if selection == get_color():
        user_bilance = user_bilance + bet * 2
        print("You won!")
    else: 
        user_bilance = user_bilance - bet
        print("You lost!")

    print("You selected: ", selection)

if __name__ == "__main__":
    start_game()
    total_counter = 0
    color = 0
    for _ in range(1_000):
        if get_color() == 2:
            color = color + 1
            total(color / total_counter * 100)
    