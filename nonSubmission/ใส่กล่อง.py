"""ใส่กล่อง"""
w, l, m, n = map(int, input().split())

optimal = {}
for i in range(m,n+1):
    optimal[i] = l%i + w%i
    if not l%i or not w%i:
        optimal[i] = 0

lowest = min(optimal, key=optimal.get)
remain_w = w % lowest
remain_l = l % lowest
print(remain_w * remain_l)
