"""[LEARNING LOGS] Point Sorting"""
def fx(x,y):
    """x+y"""
    return x+y

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    point = [0] * n
    for i in range(n):
        point[i] = list(map(int, (input().split())))
        point[i].append(fx(point[i][0],point[i][1]))
    sortedP = sorted(point, key=lambda  x:(x[2],x[0]))
    for i in range(n):
        print(sortedP[i][0], sortedP[i][1])
