def maxMin(k, arr):
    # Write your code here
    # arr.sort()
    # min_unfair = 0
    # unfairness = 0
    # for num in range(len(arr) - k + 1):
    #     unfairness = arr[num + k - 1] - arr[num]
    #     if num == 0:
    #         min_unfair = unfairness
    #     elif min_unfair > unfairness:
    #         min_unfair = unfairness
    # return min_unfair

# Same code but in one line using list comprehension
    arr.sort()
    return min(arr[num + k - 1] - arr[num] for num in range(len(arr) - k + 1))



print(maxMin(4, [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]))
print(maxMin(3, [10, 100, 300, 200, 1000, 20, 30]))
print(maxMin(2, [1, 2, 1, 2, 1]))