# https://www.hackerrank.com/challenges/one-month-preparation-kit-tower-breakers-1/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-two&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def towerBreakers(n, m):
    # Write your code here
    if m == 1 or n%2 == 0:
        return 2
    else:
        return 1
    

print(towerBreakers(2, 2))
print(towerBreakers(1, 4))
print(towerBreakers(3, 7))
print(towerBreakers(1, 7))