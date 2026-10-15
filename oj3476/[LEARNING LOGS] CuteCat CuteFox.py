"""[LEARNING LOGS] CuteCat CuteFox"""
dictcat = {}
dictfox = {}
n = int(input())
have01cat = False
have01fox = False
while n > 0:
    n -= 1
    rawinput = input().split(":")
    name = rawinput[0][2:-2:]
    num = rawinput[1][2:-2:]
    if "Cat" in num:
        num = int(str(num).split("Cat")[1])
        if num == 1:
            have01cat = True
        dictcat[name] = num
    else:
        num = int(str(num).split("Fox")[1])
        if num == 1:
            have01fox = True
        dictfox[name] = num

if not have01cat and "Garfield" not in dictcat and "Garfield" not in dictfox:
    dictcat["Garfield"] = 1
if not have01fox and "Fubuki" not in dictcat and "Fubuki" not in dictfox:
    dictfox["Fubuki"] = 1

sortDictCat = sorted(dictcat.items(), key=lambda num: num[1])
sortDictFox = sorted(dictfox.items(), key=lambda num: num[1])

print(f"Cat : {len(sortDictCat)}")
print(f"Fox : {len(sortDictFox)}")
for _, item in enumerate(sortDictCat):
    print(f"{item[0]} : Cat{item[1]:02d}")
for _, item in enumerate(sortDictFox):
    print(f"{item[0]} : Fox{item[1]:02d}")
