"""พอด"""
n, k = map(int, input().split())

row = {i:0 for i in range(1, k+1)}
sm = 0
mn = 999999999

while n>0:
    n -= 1
    passenger = int(input())
    row[passenger] += 1
    sm += 1

for i in row.values():
    if i < mn:
        mn = i

print(sm - mn*k)
