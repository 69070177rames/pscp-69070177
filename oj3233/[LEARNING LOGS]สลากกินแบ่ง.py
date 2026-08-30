"""[LEARNING LOGS] สลากกินแบ่ง"""
aksorn1, num1 = input().split()
aksorn2, num2 = input().split()

if aksorn1 == aksorn2 and num1 == num2:
    print("1000000")
elif aksorn1 != aksorn2 and num1 == num2:
    print("100000")
elif aksorn1 == aksorn2 and num1[-3::] == num2[-3::]:
    print("2000")
elif aksorn1 == aksorn2 and num1[-2::] == num2[-2::]:
    print("1000")
elif aksorn1 != aksorn2 and num1[-3::] == num2[-3::]:
    print("200")
elif aksorn1 != aksorn2 and num1[-2::] == num2[-2::]:
    print("100")
elif aksorn1 == aksorn2:
    print("20")
else:
    print("0")
