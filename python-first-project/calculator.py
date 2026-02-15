def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "cannot divide by zero"
    

while True:    
    print("\nSimple calculator")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Result:", add(num1, num2))

    elif choice == "2":
        print("Result:", subtract(num1, num2))

    elif choice == "3":
        print("Result:", multiply(num1, num2))

    elif choice == "4":
        print("Result:", divide(num1, num2))

    elif choice == "5":
        print("Exiting calculator...")
        break

    else:
        print("invalid choice")

                   