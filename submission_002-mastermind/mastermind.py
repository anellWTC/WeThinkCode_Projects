import random
from typing import List, NewType

def run_game():
    random_number = set()
    while True:
        random_number.add(random.randint(1,8))
        if len(random_number) == 4:
            break
    new_list = list(random_number)
        
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')
    turns = 12
    while turns > 0:
        answer = input("Input 4 digit code: ")
        while ("0" in answer or "9" in answer) or len(answer) != 4 or answer.isdigit() != True:
            if len(answer) != 4:
                print("Please enter exactly 4 digits.")
                answer = input("Input 4 digit code: ")
            else:
                answer = input("Input 4 digit code: ")
        answer_list = list(answer)
        # print(*new_list) # removes brackets
        # print(*answer_list)
        correct_digit = 0
        correct_digit_spot = 0
        for x in range(len(new_list)):
            for y in range(len(answer_list)):
                if int(new_list[x]) == int(answer_list[y]) and x == y:
                    correct_digit_spot += 1
                if int(new_list[x]) == int(answer_list[y]) and x != y:
                    correct_digit += 1
        print("Number of correct digits in correct place:     " + str(correct_digit_spot))
        print("Number of correct digits not in correct place: " + str(correct_digit))
        if correct_digit_spot == 4:
            print("Congratulations! You are a codebreaker!")
            break
        else:
            turns -=1
            print("Turns left: "+str(turns))
    print("The code was: ", end="")
    print(*new_list,sep="")
        
                
                
    
if __name__ == "__main__":
    run_game()
