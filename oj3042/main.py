"""divide 10"""
number = int(input())
number = number - (number%10)
while number >= 0:
    if number:
        print(number, end=" ")
    else:
        print(number, end="")
    number -= 10
