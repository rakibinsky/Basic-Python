#!/opt/homebrew/bin/python3

# For loop example
for i in range(3):
    print("Range from for loop: ", i)


# While loop example
count = 0
while count < 5:
    print("Range from while loop: ", count)
    count += 1

# Conditionals
age = int(input("Enter the age: "))
if age > 18 and age < 150:
    print("You are an adult.")
elif age > 150:
    print("R.I.P")
else:
    print("You are a minor.")

# Functions
def add_numbers(num1, num2):
    return num1 + num2

def sub_numbers(num1, num2):
    return num1 - num2

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

Summation = int (add_numbers(num1,num2))
Subtraction = int (sub_numbers(num1,num2))

print("Sum of the numbers is: ", Summation)
print("Sub of the numbers is: ", Subtraction)

