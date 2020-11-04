import random


code = [0,0,0,0]
correct = False
turns = 0
answer = ""
def random_code(): 
    """Generates random code, which the user will guess
    Within the range of 1-8"""

# TODO: Decompose into functions
    global code
    code = [0,0,0,0]
    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')


def get_guess():    #print(code)
    """Request the user to input a code
    The for loop will check if the users input matches the answer(code variable)
    -If so, it will count the amount of numbers in the correct place and number of correct digits not in correct place
    -If not the users amount of turns"""

    global correct
    global turns
    global answer
    correct = False
    turns = 0
    while not correct and turns < 12:
        answer = input("Input 4 digit code: ")
        if len(answer) < 4 or len(answer) > 4:
            print("Please enter exactly 4 digits.")
            continue
        correct_digits_and_position = 0
        correct_digits_only = 0
        for i in range(len(answer)):
            if code[i] == int(answer[i]):
                correct_digits_and_position += 1
            elif int(answer[i]) in code:
                correct_digits_only += 1

        print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
        print('Number of correct digits not in correct place: '+str(correct_digits_only))
        turns += 1

        if correct_digits_and_position == 4:
            correct = True
            print('Congratulations! You are a codebreaker!')
        else:
            print('Turns left: '+str(12 - turns))

    print('The code was: '+str(code))


def run_game():
    """Stores the functions created above"""
    random_code()
    get_guess()

if __name__ == "__main__":
    run_game()
