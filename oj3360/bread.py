"""[LEARNING LOGS] หั่นขนมปัง"""
W,H,M,N = map(int,input().split())
x = input().split()
y = input().split()
dx = []
dy = []
for i in range(M+1):
    if not i:
        dx.append(int(x[i]))
    elif i == M:
        dx.append(W - int(x[i-1]))
    else:
        dx.append(int(x[i]) - int(x[i-1]))
for i in range(N+1):
    if not i:
        dy.append(int(y[i]))
    elif i == N:
        dy.append(H - int(y[i-1]))
    else:
        dy.append(int(y[i]) - int(y[i-1]))
dx.sort(reverse=True)
dy.sort(reverse=True)
possible = []
for i in range(2):
    for j in range(2):
        possible.append(dx[i]*dy[j])
possible.sort(reverse=True)
print(possible[0], possible[1])
