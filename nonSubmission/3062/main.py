"""ticket"""

age = int(input())
S = str(input()).lower()

if age < 18 or S == "s":
    print("20")
else:
    print("50")
