# https://www.hackerrank.com/test/flgjjnhfm7i/login?b=eyJocnNjIjp0cnVlLCJocnNjX3NyYyI6ImpvYnNhcHAiLCJoaWRlIjp0cnVlLCJqb2JfaWQiOm51bGwsInVzZXJuYW1lIjoibHBsYW5jYXJ0ZUBvdXRsb29rLmNvbSIsInBhc3N3b3JkIjoiNmU1ZWM5ZTEiLCJoaWRlU3dpdGNoQWNjb3VudCI6dHJ1ZSwiaGlkZVNoYXJlSGFja2VyUHJvZmlsZSI6dHJ1ZSwiYWNjb21tb2RhdGlvbnMiOm51bGx9

# Find the median value of an array
# the process is first sorting the array and then 
# returning the value in the middle index

def findMedian(arr):
    # Write your code here
    arr.sort()
    idx = len(arr) // 2
    return arr[idx]

print(findMedian([5, 2, 6, 3, 9]))



# Flipping the matrix
# Finding the biggest sum in the upper left cuadrant of a squared matrix
# by inverting its rows and columns
# In this example, the final matrix would be:
        # [119, 114, 42, 112] 
        # [56, 125, 101, 49] 
        # [15, 78, 56, 43] 
        # [62, 98, 83, 108]
# Meaning that the numbers in the upper left cuadrant = 119, 114, 56, 125
# produce de maximum sum of numbers = 414

matrix = [[112, 42, 83, 119], 
          [56, 125, 56, 49], 
          [15, 78, 101, 43], 
          [62, 98, 114, 108]]

def flippingMatrix(matrix):
    n = int(len(matrix) / 2)
    sum = 0
    i = 0

    while (i < n) :
        j = 0
        while (j < n) :
            sum += max(max(matrix[i][j],
                           matrix[i][2 * n - j - 1]),
                       max(matrix[2 * n - i - 1][j],
                           matrix[2 * n - i - 1][2 * n - j - 1]))
            j += 1
        i += 1
    return sum

matrix_2 = [[107, 54, 128, 15],
            [12, 75, 110, 138],
            [100, 96, 34, 85],
            [75, 15, 28, 112]]

print(flippingMatrix(matrix))
print(flippingMatrix(matrix_2))