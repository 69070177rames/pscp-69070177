"""LastStand"""
l = str(input())
l = l.strip("[]").split(",")
for _, num in enumerate(l):
    print((num)[-1])
