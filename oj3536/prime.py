"""prime"""
def if_prime(n):
    """asd"""
    if n <= 1:
        return False
    if n in [2,3]:
        return True
    if not n % 2 or not n % 3:
        return False
    for i in range(5, int(n**0.5//1 + 1), 4):
        if not n % i or not n % (i+2):
            return False
    return True

def main():
    """asd"""
    a = int(input())
    if if_prime(a):
        print("YES")
    else:
        print("NO")
main()
