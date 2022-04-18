# hackerrank.com/challenges/one-month-preparation-kit-caesar-cipher-1/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-two&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def caesarCipher(s, k):
    # Write your code here
    # cipher = ''
    # for letter in s:
    #     if ord(letter) >= 65 and ord(letter) <= 90:
    #         cipher += chr((ord(letter) + k - 65) % 26 + 65)
    #     elif ord(letter) >= 97 and ord(letter) <= 122:
    #         cipher += chr((ord(letter) + k - 97) % 26 + 97)
    #     else:
    #         cipher += letter
    # return cipher

# Same code just another way of writing it
    cipher = ''
    for letter in s:
        if letter.isupper():
            cipher += chr((ord(letter) - ord('A') + k) % 26 + ord('A'))
        elif letter.islower():
            cipher += chr((ord(letter) + k - ord('a')) % 26 + ord('a'))
        else:
            cipher += letter
    return cipher

print(caesarCipher('middle-Outz', 2))
print(caesarCipher('Always-Look-on-the-Bright-Side-of-Life', 5))
print(caesarCipher('Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj', -5))