"""Cyan's password generator"""

NAME = str(input())
SUR = str(input())
AGE = str(input())

if len(NAME) >= 5 and len(SUR) >= 5:
    print(f"{NAME[0]}{NAME[1]}{SUR[-1]}{AGE[-1]}")
else:
    print(f"{NAME[0]}{AGE}{SUR[-1]}")
