"""asd"""
a = int(input())
electricity = 0
if a > 200:
    electricity += max(0, a-200) * 15
    electricity += (100 * 12) + (50 * 10) + (40 * 7) + (10 * 5)
elif a > 100:
    electricity += max(0, a-100) * 12
    electricity += (50 * 10) + (40 * 7) + (10 * 5)
elif a > 50:
    electricity += max(0, a-50) * 10
    electricity += (40 * 7) + (10 * 5)
elif a > 10:
    electricity += max(0, a-10) * 7
    electricity += 10 * 5
elif a :
    electricity += a * 5

total = electricity * 107 + a * 50
total = (total + 5) // 10
print(f"{total // 10}.{total % 10}")
