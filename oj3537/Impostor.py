"""Impostor"""
dic = {}
dead = {}
imposremain = 0
start = False
while True:
    a = input()
    if start:
        if a == "End":
            break
        dead[a] = dic[a]
        dic.pop(a)
    else:
        if a == "Start":
            start = True
        else:
            a = a.split(":")
            dic[a[0][2:-2]] = a[1][2:-2]

sortalive = dict(sorted(dic.items(), key=lambda x: x[0]))
sortdead = dict(sorted(dead.items(), key=lambda x: x[0]))
for i in sortalive.values():
    if i == "Impostor":
        imposremain+=1

print(f"{imposremain} Impostor Remains")
print("***Alive***")
for i,j in sortalive.items():
    print(f"{i} : {j}")

print("***Dead***")
for i,j in sortdead.items():
    print(f"{i} : {j}")
