# Simple Calculator Program
print("----- !! CALCULATOR BY Aayan Srivastwa  !! -----")


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

print("=== Simple Calculator ===")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

choice = input("Enter your choice (1-5): ")

if choice == "5":
    print("Exiting the calculator...")
else:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        result = add(num1, num2)
        print("Result:", result)

    elif choice == "2":
        result = subtract(num1, num2)
        print("Result:", result)

    elif choice == "3":
        result = multiply(num1, num2)
        print("Result:", result)

    elif choice == "4":
        result = divide(num1, num2)
        print("Result:", result)

    else:
        print("Invalid choice. Please restart the program.")
