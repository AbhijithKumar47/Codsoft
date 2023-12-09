class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, a, b):
        self.result = a + b

    def subtract(self, a, b):
        self.result = a - b

    def multiply(self, a, b):
        self.result = a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        self.result = a / b

def run_calculator():
    print("Welcome to the Simple Calculator program.")
    calculator = Calculator()

    while True:
        print("\nEnter your choice:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input()

        if choice == '1':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            calculator.add(num1, num2)
            print(f"Result: {calculator.result}")

        elif choice == '2':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            calculator.subtract(num1, num2)
            print(f"Result: {calculator.result}")

        elif choice == '3':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            calculator.multiply(num1, num2)
            print(f"Result: {calculator.result}")

        elif choice == '4':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            try:
                calculator.divide(num1, num2)
                print(f"Result: {calculator.result}")
            except ValueError as e:
                print(e)

        elif choice == '5':
            print("Exiting the Simple Calculator program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run_calculator()