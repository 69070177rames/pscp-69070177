"""Elon Musk"""
n, S = input().split()
for i in range(int(n)):
    for j in range(int(n)):
        if S == "#":
            if j in (i, int(n) - i - 1):
                print("#",end="")
            else:
                print("-",end="")
        else:
            if j in (i, int(n) - i - 1):
                if i < int(n)//2:
                    print(f"{chr(ord(S) + int(n)//2 - i)}",end="")
                elif i == int(n)//2:
                    print(f"{S}",end="")
                elif i > int(n)//2:
                    print(f"{chr(ord(S) + i - int(n)//2)}",end="")
            else:
                print("-",end="")
    print()
