"""theSame"""

a = float(input())
b = float(input())
c = float(input())

if a == b == c:
    print("all the same")
elif a != b and b != c and c != a:
    print("all different")
else:
    print("neither")
