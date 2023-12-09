import random

def run_rps_game():
    print("Welcome to the Rock-Paper-Scissors game.")
    scores = {'user': 0, 'computer': 0}

    while True:
        print("\nEnter your choice:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")

        choice = input()

        if choice == '4':
            print("Exiting the Rock-Paper-Scissors game.")
            break

        options = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(options)

        if choice == '1':
            user_choice = 'rock'
        elif choice == '2':
            user_choice = 'paper'
        elif choice == '3':
            user_choice = 'scissors'
        else:
            print("Invalid choice. Please try again.")
            continue

        print(f"User choice: {user_choice}")
        print(f"Computer choice: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("You win!")
            scores['user'] += 1
        else:
            print("You lose!")
            scores['computer'] += 1

        print(f"User score: {scores['user']}")
        print(f"Computer score: {scores['computer']}")

        play_again = input("Do you want to play again? (y/n): ")

        if play_again.lower() != 'y':
            break

if __name__ == "__main__":
    run_rps_game()