"""Bus Seat"""
a = int(input())
long = int(input())
iSeat = int(input())

for i in range(a,0,-1):
    row = []
    for j in range(long):
        if i+(a*j) != iSeat:
            row.append(f"{i+(a*j):02d}")
        else:
            row.append("XX")
    print(" ".join(row))
    if not (i+1) % 2 and i != 1:
        print()
