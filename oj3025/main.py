"""season"""

month = int(input())
day = int(input())

season = ["winter", "spring", "summer", "fall"]

pass21day = day >= 21

if month <= 3:
    if month == 3 and pass21day:
        print(season[1])
    else:
        print(season[0])
elif month <= 6:
    if month == 6 and pass21day:
        print(season[2])
    else:
        print(season[1])
elif month <= 9:
    if month == 9 and pass21day:
        print(season[3])
    else:
        print(season[2])
elif month <= 12:
    if month == 12 and pass21day:
        print(season[0])
    else:
        print(season[3])
