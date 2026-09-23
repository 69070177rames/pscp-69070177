"""A"""
a = set()
b = set()
n = int(input())
m = int(input())
for _ in range(n):
    a.add(int(input()))
for _ in range(m):
    b.add(int(input()))
c = a-b
c = list(c)
c.sort()
print(" ".join(map(str, c)))
