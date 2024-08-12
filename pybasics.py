
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
if age >= 18 and age <= 150:
    print("You are an adult.")
elif age > 150:
    print("RIP")
else:
    print("You are a minor.")
