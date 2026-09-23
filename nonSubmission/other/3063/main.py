"""safe password"""
AKSORN = str(input())
RAHAT = str(input())

if AKSORN == "H" and RAHAT == "4567":
    print("safe unlocked")
elif AKSORN == "H":
    print("safe locked - change digit")
elif RAHAT == "4567":
    print("safe locked - change char")
else:
    print("safe locked")
