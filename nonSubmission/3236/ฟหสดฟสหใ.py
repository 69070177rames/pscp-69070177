"""fadtake"""
n = int(input())
A = str(input())
B = str(input())
count = 0
for i in range(n):
    if int(A[i])+int(B[i]) != 9:
        count +=1

if not count:
    print("YES")
else:
    print(f"NO {count}")
