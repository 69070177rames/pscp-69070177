"""RectangleArea"""
x1, y1, wid1, hight1 = map(int , input().split())
x2, y2, wid2, hight2 = map(int , input().split())

left1, right1 = x1, x1+wid1
bottom1, top1 = y1, y1+hight1

left2, right2 = x2, x2+wid2
bottom2, top2 = y2, y2+hight2

overlapX = min(right1, right2) - max(left1, left2)
overlapY = min(top1, top2) - max(bottom1, bottom2)

if overlapX > 0 and overlapY > 0:
    print(overlapX * overlapY)
else:
    print("no overlapping")
