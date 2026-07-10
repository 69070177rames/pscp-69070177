""""[LEARNING LOGS] SurprisingVote"""

allsum = float(input())
maxScore = float(input())
if maxScore - (allsum - (maxScore*2)) <= 2:
    print("Not surprising")
else:
    print("Surprising")
