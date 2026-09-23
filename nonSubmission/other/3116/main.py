"""jkpsdfghjklp;dsftg;lpkhjsdftgkhjmdf;'thkjmdftgh;klm'"""
S = str(input()).upper()
password = []
for i in range(0,10):
    if (i+1) % 2:
        a = ord(S[0])+i
    else:
        a = ord(S[-1])-i
    a = (a%len(S)) % 10
    password.append(a)

for i in range(10):
    if 2 <= i <= 7:
        print(password[i], end=" ")
    if i == 7:
        print()
