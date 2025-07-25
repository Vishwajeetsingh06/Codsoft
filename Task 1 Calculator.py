# Simple calculator - basic version

def main():
    print("Simple Calculator")

    # Get numbers from user
    a = input("Enter first number: ")
    b = input("Enter second number: ")

    # Convert input to float
    a = float(a)
    b = float(b)

    # Ask user what they want to do
    print("Select operation:")
    print(" + for addition")
    print(" - for subtraction")
    print(" * for multiplication")
    print(" / for division")

    op = input("Enter operation: ")

    if op == '+':
        ans = a + b
        print("Result:", ans)
    elif op == '-':
        ans = a - b
        print("Result:", ans)
    elif op == '*':
        ans = a * b
        print("Result:", ans)
    elif op == '/':
        if b == 0:
            print("Cannot divide by zero")
        else:
            ans = a / b
            print("Result:", ans)
    else:
        print("Unknown operation")

main()
