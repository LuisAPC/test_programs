from cgi import test
from ctypes import cdll


test1 = [1, 2, 3, 4, 5, 6, 7, 0, -1000, 13]

def give_string(elements):
    string = ''

    for element in elements:
        if element < 1:
            string += 'Negative_or_cero '
            continue
        
        if isprime(element) == True:
            string += 'Prime '
        else:
            string += 'Composite '

    return string

def isprime(element):

    if element == 1:
        return False
    elif element < 1:
        return 'negative or cero'

    i = 2

    while i*i <= element:
        if element % i == 0:
            return False
        i += 1
    return True

    # if element > 1:  
    #     for n in range(2,element):  
    #         if (element % n) == 0:
    #             return False
    #     return True
    # else:
    #     return False


print(give_string(test1))
