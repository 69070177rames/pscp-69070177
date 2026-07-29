"""จำนวนในช่วง [A,B] ที่หารด้วย d เหลือเศษ r"""
a = int(input())
b = int(input())
d = int(input())
r = int(input())

startAt = a + (r - (a % d))
diff = b - startAt
if startAt < a:
    ans = diff // d
else:
    ans = (diff // d) + 1
print(ans)
