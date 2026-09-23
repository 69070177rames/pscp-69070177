"""light"""
color = {0:"Red", 1:"Green", 2:"Blue"}
c, n = input().split()
START = 0
if c.lower() == "r":
    START = 0
elif c.lower() == "g":
    START = 1
elif c.lower() == "b":
    START = 2

for i in range(int(n)):
    print(f"{color[(i+START)%3]}", end=" ")
