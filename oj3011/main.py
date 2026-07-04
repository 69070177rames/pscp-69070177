"""Color"""

COLOR1 = str(input()).lower()
COLOR2 = str(input()).lower()

if (COLOR1 == "red" and COLOR2 == "yellow") or (COLOR1 == "yellow" and COLOR2 == "red"):
    print("Orange")
elif (COLOR1 == "red" and COLOR2 == "blue") or (COLOR1 == "blue" and COLOR2 == "red"):
    print("Violet")
elif (COLOR1 == "yellow" and COLOR2 == "blue") or (COLOR1 == "blue" and COLOR2 == "yellow"):
    print("Green")
elif COLOR1 == COLOR2 == "red":
    print("Red")
elif COLOR1 == COLOR2 == "yellow":
    print("Yellow")
elif COLOR1 == COLOR2 == "blue":
    print("Blue")
else:
    print("Error")
