"""p"""
import json
a = json.loads(input())
n = False
for i in a:
    if not i % 2:
        print(i)
        n = True

if not n:
    print("Nope")
