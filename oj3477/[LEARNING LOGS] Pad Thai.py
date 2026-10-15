"""[LEARNING LOGS] Pad Thai"""

ingrediant = {"Pad Thai Sauce","Tofu","Pickle Turnip","Shrimp","Bean Sprouts",
              "Noodle","Chives","Lime","Egg","Oil","Peanuts"}
taste = {"Sweet","Sour","Salty"}
my = set()
myT = set()
cooked = False
while True:
    a = input()
    if cooked and a == "End":
        break
    if a == "Cook":
        cooked = True
        continue

    if not cooked:
        my.add(a)
    else:
        myT.add(a)

if not my <= ingrediant:
    print("This is not Pad Thai!!!")
elif my != ingrediant:
    print("This is bad!")
elif myT != taste:
    print("Not Bad...")
else:
    print("Delicious!")
