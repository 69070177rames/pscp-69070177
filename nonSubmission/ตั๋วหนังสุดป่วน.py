"""ตั๋วหนังสุดป่วน"""
n = int(input())
while n > 0:
    try:
        age, seat = map(int, input().split())
    except EOFError:
        break

    if age < 15:
        print("-1")
        continue

    if seat > n:
        print("-2")
        continue

    cost = 0
    if 15 <= age <= 22:
        cost = seat * 150 * 80 // 100
    elif age >= 60:
        cost = seat * 150 * 50 // 100
    else:
        cost = seat * 150

    n -= seat
    print(cost, n)
