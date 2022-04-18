# https://www.hackerrank.com/challenges/one-month-preparation-kit-drawing-book/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-two&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def pageCount(n, p):
    # Write your code here
    return min(p//2, n//2 - p//2)


print(pageCount(8 , 3))
print(pageCount(8 , 5))