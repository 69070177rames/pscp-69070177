import math
"""Elo"""

ra = int(input())
rb = int(input())
AB = str(input())
EA = 0
EB = 0
if AB == "A":
    EA = 1 / (1 + math.pow(10, (rb-ra)/400))
    print(f"{round(EA,2):.2f}")
else:
    EB = 1 / (1 + math.pow(10, (ra-rb)/400))
    print(f"{round(EB,2):.2f}")