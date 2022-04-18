# https://www.hackerrank.com/challenges/one-month-preparation-kit-dynamic-array/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-two

def dynamicArray(n, queries):
    # Write your code here
    arr = [[] for num in range(n)]
    last_answer = 0
    result_array = []
    for query in queries:
        idx = (query[1] ^ last_answer) % n
        if query[0] == 1:
            arr[idx].append(query[2])
        elif query[0] == 2:
            last_answer = arr[idx][query[2] % len(arr[idx])]
            result_array.append(last_answer)
    return result_array

print(dynamicArray(2, [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]))