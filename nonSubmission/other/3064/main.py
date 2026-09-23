"""who เกิดก่อน"""
y1 = int(input())
m1 = int(input())
d1 = int(input())
y2 = int(input())
m2 = int(input())
d2 = int(input())

def is_leap(year):
    """iLeapYear"""
    return (not year % 400) or (not year % 4 and year % 100)

def calculate(year, month, day):
    """calculate to day"""
    eachMonthHave = [31,28,31,30,31,30,31,31,30,31,30,31]

    days = (year-1) * 365
    days += (year-1) // 4
    days -= (year-1) // 100
    days += (year-1) // 400

    for i in range(month-1):
        days += eachMonthHave[i]

    if month > 2 and is_leap(year):
        days += 1

    days += day
    return days

day1 = calculate(y1,m1,d1)
day2 = calculate(y2,m2,d2)

if abs(day1 - day2) <= 7:
    print("0")
elif day1 < day2:
    print("1")
else:
    print("2")
