from itertools import count
import math

def merge(L1, L2):
  L = []
  try:
    m1 = len(L1)
    m2 = len(L2)
    c1, c2 = 0
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
  except:  
    x = 1
  return L
def mSort(L):
  global count
  print("count" + str(count))
  try:
    count += 1
  except:
    count = 0
  if len(L) > 1:
    m = math.trunc(len(L) / 2)
    print(m)
    L1 = []
    L2 = []
    for i in range(m):
      L1.append(L[i])
    for i in range(m + 1, len(L)):
      L2.append(L[i])
    return merge(mSort(L1), mSort(L2))
  else:
    return L

list = merge([1, 2, 3], [4, 5, 6])
for i in list:
  print(i, end = " ")
"""
L = mSort([1, 2, 3])
for i in L:
  print(L, end = " ")
"""
