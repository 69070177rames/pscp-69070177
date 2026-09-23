"""PickThemAgain"""
a = input().split()
b = []
for i in a[::-1]:
    if  i.isdigit() or (i.startswith('-') and i[1:].isdigit()):
        if not int(i) % 3 or not int(i) % 5:
            b.append(i)

if b:
    for x in b:
        print(x)
else:
    print("Nope")
