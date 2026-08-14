"""suvanabhumi"""
arriveH, arriveMin  = map(int, input().split("."))
outH, outMin = map(int, input().split("."))
arrive = arriveH * 60 + arriveMin
leave = outH * 60 + outMin
if leave < arrive:
    leave += 24 * 60
diff = leave - arrive

if not 0 <= arriveH <= 24 or not 0 <= arriveMin <= 59 or not 0 <= outH <= 23 or not 0 <= outMin <= 59:
    print("ERROR")
else:
    if not diff:
        print(250)
    elif diff <= 15:
        print("FREE") 
    elif diff <= 60:
        print(25)
    elif diff <= 120:
        print(50)
    elif diff <= 180:
        print(80)
    elif diff <= 240:
        print(110)
    elif diff <= 300:
        print(145)
    elif diff <= 360:
        print(180)
    elif diff <= 1440:
        print(250)
    else:
        print("ERROR")
