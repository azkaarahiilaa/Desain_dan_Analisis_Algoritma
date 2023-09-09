def getsum(myList):
    sum=0
    for row in myList:
        for item in row:
            sum += item
    return sum
getsum([[1,2,5],[3,4,7]])