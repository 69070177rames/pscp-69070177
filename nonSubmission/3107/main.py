"""บัสโน"""
pos, year, salary = input().split()
pos = pos.lower()
year = int(year)
salary = int(salary)
money = 0
if pos == "m":
    money += 1500
    if year < 5:
        money += salary * 0.06
    elif year <= 10:
        money += salary * 0.08
    else:
        money += salary * 0.10
elif pos == "b":
    money += 1000
    if year < 5:
        money += salary * 0.05
    elif year <= 10:
        money += salary * 0.06
    else:
        money += salary * 0.07
elif pos == "g":
    money += 500
    if year < 5:
        money += salary * 0.04
    elif year <= 10:
        money += salary * 0.05
    else:
        money += salary * 0.06

if year <= 0:
    money = 0
print(int(money))
