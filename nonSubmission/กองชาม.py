"""กองชาม"""
#หาจำนวนไซต์ชามเดียวกันที่มากที่สุด
n = int(input())
charmTraKai = [0]*100000
for i in range(n):
    a = int(input())
    charmTraKai[a] += 1
    i += 0
charmTraKai.sort(reverse=True)
print(charmTraKai[0])
