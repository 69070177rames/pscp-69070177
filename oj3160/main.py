"""[LEARNING LOGS] หาจำนวนเฉพาะ"""
import math
def isprime(n):
    """นี่คือด็อกสติง"""
    if n <= 1:
        return False
    if n == 2:
        return True
    if not n % 2:
        return False

    for i in range(3, int(math.sqrt(n))+1,2):
        if not n % i:
            return False
    return True

count = []
a,b = map(int,input().split())
for num in range(a,b+1):
    if isprime(num):
        count.append(num)

for idx, item in enumerate(count):
    if idx == len(count)-1:
        print(f"{item}")
    else:
        print(f"{item}",end=" ")
print(f"Total primes: {len(count)}")
