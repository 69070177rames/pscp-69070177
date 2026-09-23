"""[LEARNING LOGS] แปลงดอกไม้"""
l,n = map(int, (input().split()))
band = 1

while True:
    diagonal = band * l
    total = diagonal * (diagonal + 1) // 2

    if total >= n:
        print(band)
        break

    band += 1
