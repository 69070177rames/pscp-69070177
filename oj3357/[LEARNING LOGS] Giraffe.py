"""[LEARNING LOGS] Giraffe"""
n = int(input())
giraffe = []
count=0
for _ in range(n):
    giraffe.append(int(input()))

for idx, height in enumerate(giraffe):
    if len(giraffe) == 1:
        count+=1
        break
    if not idx and height > giraffe[idx+1]:
        count+=1
    elif idx == n-1 and height > giraffe[idx-1]:
        count+=1
    elif 0 < idx < n-1 and height > giraffe[idx+1] and height > giraffe[idx-1]:
        count+=1
print(count)
