"""[LEARNING LOGS] Shorten"""
start = -1
last = -1
numlist = []

while True:
    a = int(input())
    if a == -1:
        if start == -1 or last == -1:
            break
        if not start - last:
            numlist.append(f"{last}")
        else:
            numlist.append(f"{start}-{last}")
        break
    if start == -1:
        start = a
        last = a

    if a-last > 1:
        if not start - last:
            numlist.append(f"{last}")
        else:
            numlist.append(f"{start}-{last}")
        start = a
    last = a

print(str(numlist).strip("[]").replace("'",""))
