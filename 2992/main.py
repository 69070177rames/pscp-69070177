"""สลับหมายเลข"""

NUM = str(input())
REVERSED = int(NUM[::-1])

SIGN = str(input())
if SIGN == "+":
    print(f"{NUM} + {REVERSED} = {int(NUM) + REVERSED}")
elif SIGN == "*":
    print(f"{NUM} * {REVERSED} = {int(NUM) * REVERSED}")
