"""[LEARNING LOGS] สงคราม...ส่งด่วน"""
pointA, pointB = input().split()
kg = float(input())
way = {
    "BKK":
    {
        "CNX":{"Start": 10,"perWeight": 30},
        "PKT":{"Start": 25,"perWeight": 50}
    },

    "CNX":
    {
        "UBP":{"Start": 15,"perWeight": 40}
    },

    "UBP": 
    {
        "BKK":{"Start": 20,"perWeight": 40},
        "PKT":{"Start": 40,"perWeight": 70}
    },

    "PKT":
    {
        "CNX":{"Start": 30,"perWeight": 60}
    }
}

if pointA in way and pointB in way[pointA]:
    print(f"{way[pointA][pointB]["Start"] + way[pointA][pointB]["perWeight"] * kg:.2f}")
else:
    print("Error")
