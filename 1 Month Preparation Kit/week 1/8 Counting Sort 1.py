# https://www.hackerrank.com/challenges/one-month-preparation-kit-countingsort1/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one

def countingSort(arr):
    # Write your code here
    result = [0 for num in range(100)]
    for num in arr:
        result[num] += 1
    return result


print(countingSort([1,1,3,2,1]))