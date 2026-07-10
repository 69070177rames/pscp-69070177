"""Cokezaza007"""

cost = int(input())
bottleCap = int(input())
newCost = int(input())
want = int(input())

if bottleCap:
    if bottleCap == 1:
        asdasdas = 0
    elif not want % bottleCap:
        floor = (want // bottleCap)-1
    else:
        floor = want // bottleCap
else:
    floor = 0
promoCost = floor * newCost
normalCost = (want - floor) * cost

print(promoCost + normalCost)
