import math as math

def perm(M):
  mExt = M
  for i in range (0, len(M)):
    for j in range (0, len(M[0]) - 1):
      mExt[i].append(M[i][j])
  print(mExt)
  return 0

M = [['a11', 'a12', 'a13', 'a14'], 
    ['a21', 'a22', 'a23', 'a24'], 
    ['a31', 'a32', 'a33', 'a34'], 
    ['a41', 'a42', 'a43', 'a44']]
perm(M)