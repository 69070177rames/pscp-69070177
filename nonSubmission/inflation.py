"""?"""
from decimal import getcontext, Decimal, ROUND_DOWN

getcontext().prec = 10000000000000000
n = Decimal(input())
k = int(input().strip())

rate = Decimal("1.0381")
cent = Decimal("0.01")

value = n
for _ in range(k):
    value = (value * rate).quantize(cent, rounding=ROUND_DOWN)

value = value.quantize(cent, rounding=ROUND_DOWN)
print(f"{value:.2f}")
