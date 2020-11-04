import string
def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


def convert_to_word_list(text):
    '''
    Removing punctuation marks, converting it to lowercase and splitiing each word
    '''
    words = list(filter(lambda text: text,split(" .,;?",text.lower())))
    print(words)
    return words

def words_longer_than(length, text):
    '''
    Doing the same as previous function, then only displaying the words which have more than the minimum amount of letters required by user
    '''
    word_lengths = list(filter(lambda text: text,split(" .,;?",text.lower())))
    word_lengths = [i for i in word_lengths if len(i) >= length]
    print(word_lengths)
    return word_lengths

def words_lengths_map(text):
    '''
    Calculating the amount of letters each word contains and sorting it
    '''
    word_lengths = list(filter(lambda text: text,split(" .,;?",text.lower())))
    my_list = [len(word) for word in word_lengths]
    # print (my_list)
    my_list.sort()
    my_dict = {key: my_list.count(key) for key in my_list}
    print(my_dict)
    return my_dict

# def alphabet():
#     return("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")

def letters_count_map(text):
    '''
    Calculating the number of occurences of each letter
    '''
    # char_count = list(filter(lambda text: text,split(" .,;?",text.lower())))
    alpha = string.ascii_lowercase
    char_count = dict((x,text.lower().count(x)) for x in alpha)
    print(char_count)
    return char_count

def most_used_character(text):
    '''
    Displaying the letter which has the most occurences
    '''
    if text == "":
        return None
    else:
        alpha = string.ascii_lowercase
        char_count = dict((x,text.lower().count(x)) for x in alpha)
        popular_char = max(char_count,key = lambda x: char_count[x])
        print(popular_char)
        return popular_char

if __name__ == "__main__":
    words = convert_to_word_list("These are indeed interesting, an obvious understatement, times. What say you?")
    word_lengths = words_longer_than(6, "These are indeed interesting, an obvious understatement, times. What say you?")
    word_lengths = words_lengths_map("These are indeed interesting, an obvious understatement, times. What say you?")
    char_count = letters_count_map("These are indeed interesting, an obvious understatement, times. What say you?")
    popular_char = most_used_character('These are indeed interesting, an obvious understatement, times. What say you?')

