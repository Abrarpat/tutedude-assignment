# Taking user's name
first_name = input("Enter your first name: ")

# Welcome message
print(f"Hallo, {first_name}! Welcome to the Python program.\n")

# Taking input from the user
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

# Displaying input
print("\nYou entered:", first_number, "and", second_number)

# Operations
print("The sum is:", first_number + second_number)
print("The difference is:", first_number - second_number)
print("The product is:", first_number * second_number)

# Checking division by zero
if second_number != 0:
    print("The division is:", first_number / second_number)
else:
    print("Division not possible (cannot divide by zero)")
