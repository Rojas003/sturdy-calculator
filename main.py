from calculator import add, subtract, multiply, divide

def main():
    print("Welcome to the Calculator!")
    print("Enter 'q' at any time to quit.")

    while True:
        operation = input("\nChoose operation (add, subtract, multiply, divide): ").strip().lower()
        if operation == 'q':
            break

        if operation not in ['add', 'subtract', 'multiply', 'divide']:
            print("Invalid operation. Try again.")
            continue

        try:
            a = input("Enter first number: ")
            if a == 'q':
                break
            a = float(a)

            b = input("Enter second number: ")
            if b == 'q':
                break
            b = float(b)

            if operation == 'add':
                result = add(a, b)
            elif operation == 'subtract':
                result = subtract(a, b)
            elif operation == 'multiply':
                result = multiply(a, b)
            elif operation == 'divide':
                result = divide(a, b)

            print(f"Result: {result}")

        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except ZeroDivisionError:
            print("Cannot divide by zero.")

    print("Goodbye!")

if __name__ == "__main__":
    main()
