"""Stone Paper Scissors - a simple command-line game."""
import random

CHOICES = ["stone", "paper", "scissors"]
BEATS = {"stone": "scissors", "paper": "stone", "scissors": "paper"}


def welcome():
    return "Welcome to Stone Paper Scissors"


def get_computer_choice():
    return random.choice(CHOICES)


def get_user_choice():
    while True:
        choice = input("Enter stone, paper or scissors (or quit): ").strip().lower()
        if choice in CHOICES or choice == "quit":
            return choice
        print("Invalid choice, try again.")


def decide_winner(user, computer):
    if user == computer:
        return "tie"
    if BEATS[user] == computer:
        return "user"
    return "computer"


def main():
    print(welcome())
    user_score = computer_score = 0
    while True:
        user = get_user_choice()
        if user == "quit":
            break
        computer = get_computer_choice()
        print(f"You chose {user}, computer chose {computer}.")
        result = decide_winner(user, computer)
        if result == "user":
            user_score += 1
            print("You win this round!")
        elif result == "computer":
            computer_score += 1
            print("Computer wins this round!")
        else:
            print("It's a tie!")
        print(f"Score -> You: {user_score}, Computer: {computer_score}\n")
    print(f"Final score -> You: {user_score}, Computer: {computer_score}")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()