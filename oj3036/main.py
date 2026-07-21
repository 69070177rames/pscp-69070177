"""[LEARNING LOGS] ปราสาท"""

n = int(input())
a = 1
swap = True
while a**2 < n:
    a += 1
    swap = not swap

if n % 2:
    if not swap:
        print(((a-1)*2)-1)
    else:
        print((a-1)*2)
else:
    if not swap:
        print((a-1)*2)
    else:
        print(((a-1)*2)-1)
