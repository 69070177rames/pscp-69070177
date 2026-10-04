"""asd"""
m = int(input())
n = int(input())
g1 = []
g2 = []
intersec = []
for _ in range(m):
    g1.append(input())
for _ in range(n):
    g2.append(input())
for i in g1:
    if i in g2:
        intersec.append(i)
if intersec:
    intersec.sort(reverse=True)
    for i in intersec:
        print(i)
else:
    print("Nope")
