# Create a simple calculator that can perform basic arithmetic operations:
# - Addition
# - Subtraction
# - Multiplication
# - Division

# Defines all my functions used for this program
def Addition():
    x = float(input("Please enter a number: "))
    y = float(input("Please enter a 2nd number: "))
    print(f"Result: {x + y}")


def Subtraction():
    x = float(input("Please enter a number: "))
    y = float(input("Please enter a 2nd number: "))
    print(f"Result: {x - y}")

def Multiplication():
    x = float(input("Please enter a number: "))
    y = float(input("Please enter a 2nd number: "))
    print(f"Result: {x * y}")

def Division():
    x = float(input("Please enter a number: "))
    y = float(input("Please enter a 2nd number: "))

    if (y == 0):
        print("Please enter a number thats not 0: ")
    else:
        print(f"Result: {x / y}")

def Quit():
    print("Thank you for using the App! Goodbye!")

# Main function that handles my continous loop until user enters "5".
def Main():
    # Opening message for the user
    print("Welcome to the Calulator App!")
    print("Please Select an option by entering a number:")

    while True:
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quit")

        userSelection = input("Please select what you would like to do: ")

        if userSelection == "1":
            Addition()
        elif userSelection == "2" :
            Subtraction()
        elif userSelection == "3" :
            Multiplication()
        elif userSelection == "4" :
            Division()
        elif userSelection == "5" :
            Quit()
            break
        else:
            print("Invalid selection. Please enter a number from 1 to 5:  ")

Main()