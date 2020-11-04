#TIP: use random.randint to get a random word from the list
import random

def read_file(file_name):
    """
    TODO: Step 1 - open file and read lines as words
    """
    txt_file = open(file_name,'r').readlines()
    return txt_file


def select_random_word(words):
    """
    TODO: Step 2 - select random word from list of file
    """
    word = words[random.randint(0,len(words)-1)] #selects a random word from text file
    random_letter = list(word) #converts random word to a list
    random_letter[random.randint(0, len(random_letter)-2)] = "_" # replaces a letter with a underscore
    print("Guess the word: " + "".join(random_letter)) #joins the sentence with the random word
    return word  

def get_user_input():
    """
    TODO: Step 3 - get user input for answer
    """
    missing_letter = input("Guess the missing letter: ") 
    return missing_letter


def run_game(file_name):
    """
    This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print('The word was: '+word)


if __name__ == "__main__":
    run_game('short_words.txt')

