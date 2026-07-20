"""ห่อของขวัญ"""

r, h, takaw= map(float,input().split())

width = 2 * r + h
length = 2 * 3.14 * r + takaw

print(f"{width:.2f} {length:.2f}")
