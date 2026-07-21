"""[LEARNING LOGS] Ink"""
import math

s, n = map(int, input().split())

while n > 0:
    n -= 1
    x, y = map(int, input().split())
    dist = math.sqrt((x ** 2) + (y ** 2))
    area = 3.1416 * dist**2
    ans = area/s
    print(math.ceil(ans))
