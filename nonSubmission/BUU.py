"""rabbitBUU"""
A = str(input())
ALEK = A
A = A.upper()

mx = 0
count = 0
firstB = -1
start = False

for idx, l in enumerate(A):
    if l == "B" and firstB == -1:
        firstB = idx
    if l == "U":
        if idx > 0 and A[idx-1] == "B":
            count += 1
            start = True
        elif start:
            count += 1
    else:
        mx = max(mx, count)
        count = 0
        start = False

mx = max(mx, count)

if mx >= 2:
    print(f"Yes {mx}")
else:
    if firstB >= 0:
        print(f"{ALEK[:firstB+1]}{"U" * (len(A) - firstB - 1)}")
    else:
        LN = len(A)
        print("BUU"* (LN//3),end="")
        BUU = "BUU"
        print(BUU[:LN%3])
