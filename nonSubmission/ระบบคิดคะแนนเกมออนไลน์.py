"""ระบบคิดคะแนนเกมออนไลน์"""
x = int(input())
y = int(input())
z = int(input())

score = x+y
if z > 3:
    score = int(score * 1.5)
print(score)

ANS = 0

if score >= 1500:
    ANS = 5
elif score >= 1000:
    ANS = 4
elif score >= 500:
    ANS = 3
elif score >= 200:
    ANS = 2
elif score < 200:
    ANS = 1

print(ANS)
if ANS == 5 and z >= 7:
    print(99)
elif ANS == 4 and y > 300:
    print(88)
else:
    print(0)
