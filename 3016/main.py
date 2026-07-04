"""seven"""

pattern = [7, 9, 3, 1]
DIGIT = int(input())
num = DIGIT % 4
print(f"{pattern[num-1]}")
