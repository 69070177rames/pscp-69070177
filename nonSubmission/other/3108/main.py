"""คำนวณราคาสินค้าโปรโมชั่น"""
import math
a, b, c = map(int, input().split())

answer = a*25 + b*40 + c*55

if a+b+c >= 3:
    answer *= 0.9

print(int(math.floor(answer)))
