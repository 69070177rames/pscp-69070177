"""[LEARNING LOGS] สหกรณ์โรงเรียน"""
isStudent = input()
n = int(input())
pay = 0
while n > 0:
    n -= 1
    pay += float(input())

if isStudent == "Y":
    pay *= 0.95
elif isStudent == "N" and pay >= 500:
    pay *= 0.97

if int(str(f"{pay:.3f}")[-1]) >= 5:
    print(f"{pay+0.01:.2f}")
else:
    print(f"{pay:.2f}")
