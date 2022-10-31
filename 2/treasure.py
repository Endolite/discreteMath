def merge(L1, L2):
  L = []
  m1 = len(L1)
  m2 = len(L2)
  c1 = 0
  c2 = 0
  while (c1 < m1 and c2 < m2):
      if (L1[0] < L2[0]):
          L.append(L1[0])
          L1.pop(0)
          c1 += 1
      else:
        L.append(L2[0])
        L2.pop(0)
        c2 += 1
      if (c1 == m1):
        while (c2 < m2):
          L.append(L2[0])
          L2.pop(0)
          c2 += 1
      if (c2 == m2):
        while (c1 < m1):
          L.append(L1[0])
          L1.pop(0)
          c1 += 1
  return L

def mSort(L):
  if len(L) > 1:
    m = math.trunc(len(L) / 2)
    L1 = []
    L2 = []
    for i in range(m):
      L1.append(L[i])
    for i in range(m, len(L)):
      L2.append(L[i])
    return merge(mSort(L1), mSort(L2))
  else:
    return L

pointVals = [[110, 16, 25, 78, 59],
              [65, 69, 54, 28, 71],
              [19, 93, 45, 45, 9], 
              [89, 17, 77, 18, 39],
              [37, 115, 87, 59, 97],
              [89, 102, 98, 74, 61],
              [78, 27, 99, 91, 5],
              [88, 97, 99, 99, 51]]
weightVals = [[95, 1, 21, 66, 59],
              [54, 54, 44, 26, 60],
              [3, 91, 43, 42, 5],
              [72, 30, 56, 72, 9],
              [44, 1, 71, 13, 27],
              [20, 99, 87, 52, 85],
              [72, 96, 97, 73, 49],
              [75, 82, 83, 44, 59],
              [68, 8, 87, 74, 4],
              [69, 83, 98, 88, 45]]
eff = [[0 for i in range(len(pointVals[0]))] for j in range(len(pointVals))]
temp = eff
for i in range(len(eff) - 1):
  mSort(eff[i])r
maxWeight = [91, 87, 109, 88, 64]
