"""[LEARNING LOGS] หุ่นยนต์เคาะเสียงกระเบื้อง"""
n, pay = map(int, input().split())
nxn = [[0]]*n
col = [0]*n
colsum = [0]*n
for i in range(n):
    nxn[i] = list(map(int, input().split()))
    count = 0
    for index,j in enumerate(nxn[i]):
        if j:
            col[index] += 1
            colsum[index] += j
            count += 1
    sm = sum(nxn[i])
    nxn[i].append(count)
    nxn[i].append(sm)

for i in nxn:
    print(" ".join(list(map(str, i))))
print(" ".join(list(map(str,col))))
print(" ".join(list(map(str,colsum))))
print(f"{sum(col)} {sum(colsum)} {sum(colsum) * pay:.2f}")
