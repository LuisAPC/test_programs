# https://www.hackerrank.com/challenges/one-month-preparation-kit-mini-max-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one

def miniMaxSum(arr):
    # Write your code here
# Previous version, I found out that, since I am usint .sort()
# the time complexity is O(n*logn)
    # arr.sort()
    # min_arr = arr[:-1]
    # max_arr = arr[1:]
    # max_sum = sum(max_arr)
    # min_sum = sum(min_arr)

# By using this approach, since I am using min() and max()
# the time complexity is O(n)
    elem_sum = sum(arr)
    max_sum = elem_sum - max(arr)
    min_sum = elem_sum - min(arr)
    
    print(f"{min_sum} {max_sum}")

miniMaxSum([5,2,3,4,1])