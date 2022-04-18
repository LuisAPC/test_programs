# https://www.hackerrank.com/challenges/one-month-preparation-kit-sock-merchant/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-two

def sockMerchant(n, ar):
    # Write your code here
    # total_pairs = 0
    # while ar:
    #     element =  ar[0]
    #     repetitions = ar.count(element)
    #     if repetitions < 2:
    #         ar.remove(element)
    #         continue
    #     total_pairs += repetitions // 2
    #     for repeated in range(repetitions):
    #         ar.remove(element)
    # return total_pairs

# Cleaner solution using a HashTable
    for num in ar:
        table = {}
        pairs = 0
        for num in ar:
            if num in table:
                pairs += 1
                table.pop(num)
            else:
                table[num] = 1
        return pairs

ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print(sockMerchant(len(ar), ar))