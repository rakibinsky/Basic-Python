# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Choose operation
operation = input("Enter '+' for addition or '-' for subtraction: ")

# Perform the operation and display the result
if operation == '+':
    result = num1 + num2
    print(f"The result of adding {num1} and {num2} is: {result}")
elif operation == '-':
    result = num1 - num2
    print(f"The result of subtracting {num2} from {num1} is: {result}")
else:
    print("Invalid operation. Please enter '+' or '-'.")
