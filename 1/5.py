import math
import random

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

L = [random.randint(0, 100) for i in range(10)]
print(L)
print(mSort(L))

