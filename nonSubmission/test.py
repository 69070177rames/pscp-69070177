"""asd"""
a = []
while True:
    word = input()
    if word == "NULL":
        break
    a.append(word)
for i in range(len(a)-1,-1,-1):
    print(a[i])
