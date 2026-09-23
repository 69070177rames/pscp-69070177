"""ramex"""

size, normal = input().split()
topping = input()
n = 0
if len(topping) > 1:
    n = int(topping[2:])

pay = 0
if size == "S":
    if normal == "R":
        pay += 60
    elif normal == "T":
        pay += 80
elif size == "M":
    if normal == "R":
        pay += 80
    elif normal == "T":
        pay += 100
elif size == "L":
    if normal == "R":
        pay += 100
    elif normal == "T":
        pay += 120

if topping[0] == "P":
    pay += n*15
elif topping[0] == "E":
    pay += n*10

print(pay)
