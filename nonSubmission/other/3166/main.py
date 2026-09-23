"""passornot"""
n = int(input())
m = n
score = 0
fail = False

while m > 0:
    m -= 1
    a = int(input())
    score += a
    if a < 50:
        fail = True

print(f"{score/n:.1f}")
if float(f"{score/n:.1f}") >= 60 and not fail:
    print("PASS")
else:
    print("FAIL")
