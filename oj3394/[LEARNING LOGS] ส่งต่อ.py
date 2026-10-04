"""[LEARNING LOGS] ส่งต่อ"""
n, select = map(int, input().split())
table = []
current = select
count = 0
visited = set()

while n > 0:
    n -= 1
    table.append(int(input()))

while current and current not in visited:
    visited.add(current)
    count +=1
    current = table[current-1]

print(count)
