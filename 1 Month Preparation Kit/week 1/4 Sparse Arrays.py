# https://www.hackerrank.com/challenges/one-month-preparation-kit-sparse-arrays/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one

def matchingStrings(strings, queries):
    # Write your code here
    frequency_arr = []
# 1st approach
    # for query in queries:
    #     frequency = 0
    #     for string in strings:
    #         if query == string:
    #             frequency += 1
    #     frequency_arr.append(frequency)
    # return frequency_arr

#2nd approach, which I think is the same time complexity but it is move "elegant"
    for query in queries:
        frequency_arr.append(strings.count(query))
    return frequency_arr
        


print(matchingStrings(['aba', 'baba', 'aba', 'xzxb'], ['aba', 'xzxb', 'ab']))