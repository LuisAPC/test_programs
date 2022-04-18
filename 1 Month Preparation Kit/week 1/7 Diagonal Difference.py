# https://www.hackerrank.com/challenges/one-month-preparation-kit-diagonal-difference/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one

def diagonalDifference(arr):
    # Write your code here
    sum_1 = 0
    sum_2 = 0
    for i in range(len(arr)):
        sum_1 += arr[i][i]
        sum_2 += arr[i][len(arr)-i-1]
    return abs(sum_1 - sum_2)


list_1 = [[11, 2, 4],
          [4, 5, 6],
          [10, 8, -12]]

print(diagonalDifference(list_1))