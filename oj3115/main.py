"""[LEARNING LOGS] Arcade of Time: Store Check"""

num, check = map(int ,input().split())
a = list(range(num))
idx = 0
check += 0
while num > 0:
    num -= 1
    openT, close = map(int ,input().split())
    a[idx] = [openT,close]
    idx += 1
when = list(map(int, input().split()))
cnt = 0
for i in when:
    for j in a:
        if j[0] <= i < j[1]:
            cnt += 1
    if i == when[-1]:
        print(cnt, end="")
    else:
        print(cnt, end=" ")
    cnt = 0
