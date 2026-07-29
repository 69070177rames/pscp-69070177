"""sa parn brick"""

small = int(input())
big = int(input())
goal = int(input())

greedy = min((goal // 5), big)
remain = goal - greedy*5

if big >= greedy and small >= remain and greedy*5+remain == goal :
    print(remain)
else:
    print("-1")
