"""pair"""
w = {}
a = input()
for i in a:
    if i in w:
        w[i] += 1
    else:
        w[i] = 1

ans = ""
for i,j in w.items():
    if j % 2:
        ans += i

if not ans:
    print("fully paired")
else:
    print(ans)
