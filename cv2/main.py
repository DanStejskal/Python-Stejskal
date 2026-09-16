from random import random

def get_color():
    value = random() * 100

    if value <= 3:
        return 2
    elif value <= 51.5:
        return 0
    else:
        return 1

def start_game():
    print("Welcome to Casino Royal")
    user_balance = 1000

    while True:
        bet_input = input("Enter your bet: ")

        if not bet_input.isdigit():
            print("Please enter a number!")
            continue

        bet = int(bet_input)

        if bet <= 0:
            print("Bet must be greater than 0!")
            continue

        if bet > user_balance:
            print("Not enough cash!")
            continue

        print("Select color:")
        print("\t0 - Red")
        print("\t1 - Black")
        print("\t2 - Green")
        print("\t9 - Leave game")

        selection_input = input("Enter your choice: ")

        if not selection_input.isdigit():
            print("Please enter a number!")
            continue

        selection = int(selection_input)

        if selection == 9:
            print("Thanks for playing!")
            return

        if selection not in (0, 1, 2):
            print("Invalid choice!")
            continue

        if selection == get_color():
            user_balance += bet * 2
            print("You won!")
        else:
            user_balance -= bet
            print("You lost!")

        print("You selected:", selection)
        print("Your balance:", user_balance)

        if user_balance == 0:
            print("You have no money left!")
            return

if __name__ == "__main__":
    start_game()
