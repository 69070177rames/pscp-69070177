""""Safe Password"""

password = ["H","4567"]

A = str(input())
B = str(input())

if A == password[0] and B == password[1]:
    print("safe unlocked")
elif A == password[0]:
    print("safe locked - change digit")
elif B == password[1]:
    print("safe locked - change char")
else:
    print("safe locked")
