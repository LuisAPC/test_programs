# https://www.hackerrank.com/challenges/one-month-preparation-kit-pangrams/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one

def pangrams(s):
    # Write your code here
# The other code is cleaner, but only works with the restriction that
# you will not recieve any special characters, this function however 
# is more robust and works in any case
    # abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    # sentence = s.lower()
    # for letter in sentence:
    #     if sentence.find(abc[0]) == -1:
    #         return 'not pangram'
    #     abc.pop(0)
    #     if len(abc) == 0:
    #         return 'pangram'
    # return 'not pangram'

#learned to use sets
    unique_letters = set(s.lower())
    if ' ' in unique_letters:
        unique_letters.remove(' ')
    if len(unique_letters) == 26:
        return 'pangram'
    else:
        return 'not pangram'


print(pangrams('We promptly judged antique ivory buckles for the next prize'))
print(pangrams('hello'))
print(pangrams('a'))
print(pangrams('abcdefghijklmnopqrstuvwxyz'))