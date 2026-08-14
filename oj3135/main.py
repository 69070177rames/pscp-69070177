"""[LEARNING LOGS] ของขวัญและขโมย"""
n, k, t = map(int,input().split())
i = 0
while True:
    i += 1
    if n == 1 or t == 1:
        print(1)
        break
    if (1 + k*i - 1) % n + 1 == 1:
        print(i)
        break
    if (1 + k*i - 1) % n + 1 == t:
        print(i+1)
        break
