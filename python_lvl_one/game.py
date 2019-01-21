###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!


import random

# Greets user
def greet():
    return print("""
                 Hello and welcome to a Guess Game!
                 The 3-digit code has been generated for you.
                 """)


# Random code generator
def codeGen():
    """
    Returns a list of a random 3-digit code, each number is a string element
    """
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:3]

# Get code from user
def getCode():
    """
    Gets 3-digit code from user, each number is a string element
    """
    userCode = input("Type in your guess: ")
    return list(userCode)

# Checker
def checker(generatedCode, userCode):
    """
    Checks if user has guessed
    """
    if generatedCode == userCode:
        return 'Guessed'
    else:
        for i in range(0,3):
            if generatedCode[i] == userCode[i]:
                return 'Match'
            elif userCode[i] in generatedCode:
                return 'Close'
            else:
                return 'Nope'

# Game logic
def game():
    is_running = True
    code = codeGen()
    greet()
    # Game is running
    while is_running:
        userCode = getCode()
        condition = checker(code, userCode)
        if condition == 'Guessed':
            print("You won!")
            is_running = False

game()
