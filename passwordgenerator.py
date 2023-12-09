import random
import string

class PasswordGenerator:
    def __init__(self):
        self.password = ''

    def generate(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        self.password = ''.join(random.choice(characters) for i in range(length))

def run_password_generator():
    print("Welcome to the Password Generator program.")
    password_generator = PasswordGenerator()

    while True:
        print("\nEnter your choice:")
        print("1. Generate a Password")
        print("2. Exit")

        choice = input()

        if choice == '1':
            length = int(input("Enter the desired length of the password: "))
            password_generator.generate(length)
            print(f"Generated Password: {password_generator.password}")

        elif choice == '2':
            print("Exiting the Password Generator program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run_password_generator()
