"""ชานมไข่มุก"""
bubble, bgram = input().split()
tea, sweet, cc = input().split()

bgram = float(bgram)
sweet = int(sweet)
cc = float(cc)

ans = 0.0
if bubble == "H":
    ans += 5*bgram
elif bubble == "O":
    ans += 3*bgram
elif bubble == "J":
    ans += 2*bgram

if tea == "R":
    if sweet == 1:
        ans += 12*cc
    elif sweet == 2:
        ans += 18*cc
    elif sweet == 3:
        ans += 25*cc
elif tea == "T":
    if sweet == 1:
        ans += 15*cc
    elif sweet == 2:
        ans += 20*cc
    elif sweet == 3:
        ans += 30*cc
elif tea == "M":
    if sweet == 1:
        ans += 10*cc
    elif sweet == 2:
        ans += 15*cc
    elif sweet == 3:
        ans += 20*cc

if ans.is_integer():
    print(int(ans))
else:
    print(ans)
