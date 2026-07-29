"""roman"""

a = int(input())
if a < 0:
    print("Error : Please input positive number")
elif a == 1:
    print("I")
elif a == 2:
    print("II")
elif a == 3:
    print("III")
elif a == 4:
    print("IV")
elif a == 5:
    print("V")
elif a == 6:
    print("VI")
elif a == 7:
    print("VII")
elif a == 8:
    print("VIII")
elif a == 9:
    print("IX")
else:
    print("Error : Out of range")
