# https://www.hackerrank.com/challenges/one-month-preparation-kit-two-arrays/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one

def twoArrays(k, A, B):
    # Write your code here
    A.sort()
    B.sort(reverse = True)
    for num in range(len(A)):
        if A[num] + B[num] < k:
            return 'NO'
    return 'YES'


print(twoArrays(10, [2, 1, 3], [7, 8, 9]))
print(twoArrays(5, [1, 2, 2, 1], [3, 3, 3, 4]))