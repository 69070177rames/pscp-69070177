"""รับค่า string เข้ามา 5 บรรทัด และแสดงค่าตัวอักษรที่อยู่ใน string 
นั้นในกรอบรูปสี่เหลี่ยม ดังตัวอย่างใน test case ด้านล่าง
Input Specification
ข้อความขนาดตั้งแต่ 0 ตัวอักษร (ที่เป็น a-z, A-Z, 0-9 และเว้นวรรค)  เป็นต้นไป จำนวน 5 บรรทัด


แนะนำว่าให้ทดสอบ Sample test cases โดยการ copy Input

Output Specification
ข้อความจำนวน 7 บรรทัดโดยจะมี space ระหว่างข้อความและกรอบ
ซ้ายและขวาด้านละ  1 ช่อง ตามตัวอย่าง

"""

a = []
mx = -1
for i in range(5):
    X = str(input())
    X = X.strip()
    if len(X) >= mx:
        mx = len(X)
    a.append(X)

for i in range(7):
    if not i or i == 6:
        print("*"*int(mx+4))
    else:
        print("* ",end="")
        print(a[i-1],end="")
        print(" " * int(mx - len(a[i-1])),end="")
        print(" *")
