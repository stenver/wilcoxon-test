
def calculate(pTable, gaussianPTable, verbose = False):
  approximateTable = []
  for i in range(len(pTable)):
    points = getKRelativeValues(i, pTable, gaussianPTable)
    approximateTable.append(calculateApproximateRow(points))
    if verbose:
      if(i%10 == 0): print(i)
  return approximateTable

def getKRelativeValues(n, pTable, gaussianPTable):
    pRelativeValues = []
    for j in range(len(pTable[n])):
      relativeValue = pTable[n][j] / gaussianPTable[n][j]
      pRelativeValues.append(relativeValue)
      if(pTable[n][j] == 0):
          break
    return pRelativeValues

def calculateApproximateRow(actualPoints):
  approximatedPoints = []
  currentPoint = 0
  approximatedPoints.append([currentPoint, actualPoints[currentPoint]])

  while(currentPoint != len(actualPoints) - 1):
    nextPoint = getNextApproximatedPoint(actualPoints, currentPoint)
    approximatedPoints.append([nextPoint, actualPoints[nextPoint]])
    currentPoint = nextPoint
  return approximatedPoints

def getNextApproximatedPoint(actualPoints, currentPoint):
  nextPoint = currentPoint + 1
  savedNextPoint = nextPoint

  while(canApproximate(actualPoints, currentPoint, nextPoint)):
    if(nextPoint == len(actualPoints) - 1):
      break
    savedNextPoint = nextPoint
    nextPoint += 1

  return savedNextPoint

def canApproximate(actualPoints, currentPoint, nextPoint):
  startValue = actualPoints[currentPoint]
  endValue = actualPoints[nextPoint]

  for i in range(1, nextPoint - currentPoint):
    approximatePoint = currentPoint + i
    actualValue = actualPoints[approximatePoint]
    approximateValue = linearInterpolate(approximatePoint, currentPoint, nextPoint, startValue, endValue)
    if approximateValue == 0:
      return True

    relativeAccuaracy = actualValue / approximateValue

    if relativeAccuaracy < 0.9 or relativeAccuaracy > 1.1:
      return False
  return True

def linearInterpolate(approximatePoint, endPoint, startPoint, endValue, startValue):
  return startValue + ((endValue - startValue) * (approximatePoint - startPoint) / (endPoint - startPoint))

def printKRelativeValuesForR(n, pTable, gaussianPTable):
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

def write(approximateTable, verbose = False):
  f = open('approximateTable' + str(len(approximateTable) - 1) + '.txt', 'w')
  for i in range(len(approximateTable)):
    f.write(str(approximateTable[i]))
    f.write("\n")
    if(i%10 == 0 and verbose): print(i)
  f.close()
  if(verbose):
    print('approximateTable file created')
