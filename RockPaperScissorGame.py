import random

def get_user_choice():
    print("Choices: rock, paper, scissors")
    choice = input("Enter your choice: ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please try again.")
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
    return choice

def get_computer_choice():
    options = ['rock', 'paper', 'scissors']
    return random.choice(options)

def decide_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play():
    print("=== Rock Paper Scissors Game ===")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = decide_winner(user_choice, computer_choice)
        print(f"\nResult: {result}\n")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

play()
