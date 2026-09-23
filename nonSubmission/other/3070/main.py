"""even odd"""
a = int(input())
b = int(input())
c = int(input())

even = 0
odd = 0
if a % 2:
    odd += 1
else:
    even += 1
if b % 2:
    odd += 1
else:
    even += 1
if c % 2:
    odd += 1
else:
    even += 1

print(even)
print(odd)
