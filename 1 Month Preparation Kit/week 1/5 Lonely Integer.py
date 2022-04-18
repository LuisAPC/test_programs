# https://www.hackerrank.com/challenges/one-month-preparation-kit-lonely-integer/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one

def lonelyinteger(a):
    # Write your code here
    unique_num = 0
    for num in a:
        unique_num ^= num
    return unique_num


print(lonelyinteger([1, 2, 2, 4, 3, 3, 1, 7, 7]))