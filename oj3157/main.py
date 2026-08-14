"""sasom"""
n = int(input())
score = 0
while n > 0:
    n -= 1
    KANAN = str(input())
    if KANAN == "+":
        score += 10
    elif KANAN == "-":
        score -= 5
print(score)
