# def isInt(num):
#     if(num.isint):
#         print(num)

# input("Enter number")

# Get user input or define a variable
user_input = input("Enter something: ")

# Check if the input is an integer
def isInt(user_input):
    if isinstance(user_input, int):
        print("The input is an integer.")
        return True
    else:
        print("The input is not an integer.")
        return False
def isFloat(user_input):
    if isinstance(user_input, float):
        print("The input is a float.")
        return True
    else:
        print("The input is not a float.")
        return False

# isInt(user_input)
isFloat(user_input)