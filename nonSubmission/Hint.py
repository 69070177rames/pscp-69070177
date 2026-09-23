"""Hint"""
def check_sign(a:str):
    """check sign"""
    b = []
    if a.startswith(">="):
        b = list(i for i in range(int(a[-1]),10))
    elif a.startswith("<="):
        b = list(i for i in range(0,int(a[-1])+1))
    elif a.startswith("=="):
        b = list(str(a[-1]))
    elif a.startswith("!="):
        b = list(i for i in range(0,10) if i != int(a[-1]))
    elif a.startswith(">"):
        b = list(i for i in range(int(a[-1])+1,10))
    elif a.startswith("<"):
        b = list(i for i in range(0,int(a[-1])))
    return b

one = check_sign(input())
ten = check_sign(input())
hundred = check_sign(input())

for i in hundred:
    for j in ten:
        for k in one:
            print(f"{i}{j}{k}")
