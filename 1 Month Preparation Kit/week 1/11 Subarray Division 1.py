# https://www.hackerrank.com/challenges/one-month-preparation-kit-the-birthday-bar/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one

def birthday(s, d, m):
    # Write your code here
# Nice logic, should review this to get used to this solutions
    count = 0
    for i in range(len(s)):
        if sum(s[i:i+m]) == d:
            count += 1
    return count

print(birthday([2, 2, 1, 3, 2], 4, 2))