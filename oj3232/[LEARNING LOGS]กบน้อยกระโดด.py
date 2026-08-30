"""jump"""
x, y = map(int, input().split())
c = 0
while x > 0:
    y -= x
    x -= 2
    c += 1
    if y <= 0:
        break

if y <= 0:
    print(c)
else:
    print(-1)
