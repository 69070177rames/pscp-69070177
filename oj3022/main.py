"""Temperature"""

def _to_(temp, fr):
    """Doc"""
    if fr == "F":
        a = (temp-32) * 5 / 9
    elif fr == "R":
        a = temp * 5 / 9 - 273.15
    else:
        a = temp - 273.15
    return a

def main():
    """Main"""
    temp = float(input())
    fromWhat = str(input())
    toWhat = str(input())
    if fromWhat != "C":
        C = _to_(temp, fromWhat)
    else:
        C = temp

    if toWhat == "K":
        print(f"{C + 273.15:.2f}")
    elif toWhat == "F":
        print(f"{C * 9 / 5 + 32:.2f}")
    elif toWhat == "R":
        print(f"{(C + 273.15) * 9 / 5:.2f}")
    elif toWhat == "C":
        print(f"{C:.2f}")

main()
