def linearInterpolate(approximatePoint, endPoint, startPoint, endValue, startValue):
  return startValue + ((endValue - startValue) * (approximatePoint - startPoint) / (endPoint - startPoint))

def canApproximate(actualPoints, currentPoint, nextPoint):
  startValue = actualPoints[currentPoint]
  endValue = actualPoints[nextPoint]

  for i in range(1, nextPoint - currentPoint):
    approximatePoint = currentPoint + i
    trueValue = actualPoints[approximatePoint]
    approximateValue = linearInterpolate(approximatePoint, currentPoint, nextPoint, startValue, endValue)
    if approximateValue == 0:
      return True

    relativeAccuaracy = trueValue / approximateValue

    if relativeAccuaracy < 0.9 or relativeAccuaracy > 1.1:
      return False
  return True

def getNextApproximatedPoint(actualPoints, currentPoint):
  nextPoint = currentPoint + 1

  while(canApproximate(actualPoints, currentPoint, nextPoint)):
    if(nextPoint == len(actualPoints) - 1):
      break
    nextPoint += 1
  return nextPoint

def calculateApproximateRow(actualPoints):
  approximatedPoints = []
  currentPoint = 0
  approximatedPoints.append([currentPoint, actualPoints[currentPoint]])

  while(currentPoint != len(actualPoints) - 1):
    nextPoint = getNextApproximatedPoint(actualPoints, currentPoint)
    approximatedPoints.append([nextPoint, actualPoints[nextPoint]])
    currentPoint = nextPoint
  return approximatedPoints

def getKRelativeValues(n, pTable, gaussianPTable):
    pRelativeValues = []
    for j in range(len(pTable[n])):
      relativeValue = pTable[n][j] / gaussianPTable[n][j]
      pRelativeValues.append(relativeValue)
      if(pTable[n][j] == 0):
          break
    return pRelativeValues

def calculateApproximateTable(pTable, gaussianPTable):
  approximateTable = []
  for i in range(len(pTable)):
    points = getKRelativeValues(i, pTable, gaussianPTable)
    approximateTable.append(calculateApproximateRow(points))
    if(i%10 == 0): print(i)
  return approximateTable

def printKRelativeValues(n, pTable, gaussianPTable):
    relativeValues = getKRelativeValues(n, pTable, gaussianPTable)
    #print(len(relativeValues))
    print("relativeValues <- c(", end="")
    first = True
    for i in range(len(relativeValues)):
        if(relativeValues[i] == 0):
            break
        if(not first):
            print(", ", end="")
        print(relativeValues[i], end="")
        first = False
    print(")")

def writeApproximateTableFile(approximateTable, nSize):
  f = open('approximateTable' + str(nSize) + '.txt', 'w')
  for i in range(len(approximateTable)):
    f.write(str(approximateTable[i]))
    f.write("\n")
    if(i%10 == 0): print(i)
  f.close()
  print('approximateTable file created')
