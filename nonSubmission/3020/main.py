"""Cokezaza007"""

cost = int(input())
bottleCap = int(input())
newCost = int(input())
want = int(input())

if bottleCap and want > 0:
    if not want % bottleCap :
        PROMO = (want // bottleCap)-1
    else:
        PROMO = want // bottleCap
else:
    PROMO = 0
promoCost = PROMO * newCost
normalCost = (want - PROMO) * cost

print(promoCost + normalCost)
