"""A-E-I-O-U"""
sala ={"a" : 0,"e" : 0,"i" : 0,"o" : 0,"u" : 0}
KORKARM = str(input()).lower()
for j in KORKARM:
    if j == "a":
        sala["a"] += 1
    elif j == "e":
        sala["e"] += 1
    elif j == "i":
        sala["i"] += 1
    elif j == "o":
        sala["o"] += 1
    elif j == "u":
        sala["u"] += 1

for i,j in sala.items():
    if j:
        print(f"{i} : {j}")
