"""สมดุลย์ชีวิต"""
n = int(input())
heavywork = 0
lightwork = 0
for i in range(n):
    hi = int(input())
    if hi > 18:
        heavywork += 1
    else:
        lightwork += 1
    i += 0

if lightwork > heavywork:
    print(n)
else:
    print(n+ max(0,heavywork-lightwork-1))
