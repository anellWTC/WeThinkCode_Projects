def find_min(element):
    """ Checks if the variable element is a list "type" or if the length of the element is equal to zero"""
    """TODO: complete for Step 1"""
    if type(element) != list or len(element) == 0:
        return -1 
    for i in element:
        if type(i)!= int or i == "":
            return -1
    """ Checking if the first index of the list is greater than the second index,
        if so it will delete the value that is greater.That is how the min(smallest digit in list) is decided"""
    if len(element) != 1:
        if element[0] >= element[1]:
            del(element[0])
        else:
            del(element[1])
        find_min(element)
    
    return element[0]


def sum_all(element):
    """TODO: complete for Step 2"""
    if type(element) != list or len(element) == 0:
        return -1
    for i in element:
        if type(i)!= int or i == "":
            return -1
    """Creating an addition function without using the sum function"""     
    if len(element) != 1:
        element[0] = element[0] + element[1]
        del(element[1])
        return sum_all(element)
    else:
        return element[0]



def find_possible_strings(character_set, n):
    """TODO: complete for Step 3"""
    strings = []
    for i in character_set:
       if type(i) != str :
        return []
    if n == 1:
        return character_set
    elif n > 1:
        for i in character_set:
            for item in find_possible_strings(character_set,n-1):
                strings += [i + item]
    else:
        return[]
    return strings


if __name__ == "__main__":  
    element = [3,6,8,9,2,11]
    print(find_min(element))
    element = [3,6,8,9,2,12]
    print(sum_all(element))
    character_set = []