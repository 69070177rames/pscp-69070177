""""3017"""

Bill = int(input())
Bill += min(max(50, Bill * 0.1),1000)
Bill += Bill *.07
print(f"{Bill:.2f}")
