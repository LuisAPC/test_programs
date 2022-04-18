# https://www.hackerrank.com/challenges/one-month-preparation-kit-grid-challenge/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-two&h_r=next-challenge&h_v=zen

def gridChallenge(grid):
    # Write your code here
    sorted_data = ''
    sorted_grid = []
    for data in grid:
        sorted_data = ''.join(sorted(data))
        sorted_grid.append(sorted_data)
# This part of code worked for the mayor part of cases, but 
# it failed in one case and couldn't find the cause
    # alphabetical_grid = sorted(sorted_grid)
    # if sorted_grid == alphabetical_grid:
    #     return 'YES'
    # else:
    #     return 'NO'

# This part compares letter by letter and it passes every test case
    columns = len(sorted_grid[0])
    rows = len(sorted_grid)
    for column in range(columns):
        for row in range(1, rows):
            if sorted_grid[row - 1][column] > sorted_grid[row][column]:
                return 'NO'
    return 'YES'


print(gridChallenge(['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']))
print(gridChallenge(['mpxz', 'abcd', 'wlmf']))