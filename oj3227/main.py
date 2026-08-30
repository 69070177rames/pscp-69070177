"""card"""
dict1 = {"A": "ace","J": "jack", "Q": "queen", "K": "king"}
dict2 = {"D": "diamonds", "H": "hearts", "S": "spades","C": "clubs"}
N = str(input())
if N[0].isalpha():
    print(f"{dict1[N[0].upper()]} of {dict2[N[1].upper()]}")
else:
    if N[0] == "1":
        print(f"10 of {dict2[N[2].upper()]}")
    else:
        print(f"{N[0]} of {dict2[N[1].upper()]}")
