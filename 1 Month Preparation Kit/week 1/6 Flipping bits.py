# https://www.hackerrank.com/challenges/one-month-preparation-kit-flipping-bits/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one

def flippingBits(n):
    # Write your code here
    return 2**32 + ~n

print(flippingBits(2147483647))
print(flippingBits(1))
print(flippingBits(0))