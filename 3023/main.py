"""calculater"""

N = str(input())

if N == "1":
    print("1")
else:
    SIGN = int(N)
    count = 0
    for i in range(1,int(N)+1):
        count += len(str(i))
    print(f"{count + SIGN}")
