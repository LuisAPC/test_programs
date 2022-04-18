# https://www.hackerrank.com/challenges/one-month-preparation-kit-time-conversion/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one

def timeConversion(s):
    # Write your code here
    morning = s[-2:]
    hour = s[:2]
    if morning == 'AM':
        if hour == '12':
            return '00' + s[2:-2]
        else:
            return s[:-2]
    else:
        if hour == '12':
            return s[:-2]
        else:
            pm_hour = int(hour) + 12
            return str(pm_hour) + s[2:-2]



print(timeConversion('07:05:45PM'))
print(timeConversion('12:05:50AM'))
print(timeConversion('12:00:45PM'))
print(timeConversion('04:00:00AM'))