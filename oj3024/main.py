""""[LEARNING LOGS] SurprisingVote"""

allsum = float(input())
maxScore = float(input())
if maxScore - max(0,(allsum - (maxScore*2))) <= 2:
    print("Not surprising")
else:
    print("Surprising")
