def baseConv(n, b1, b2):
  n10 = int(str(n), base = b1)
  digs = []
  pV = b2
  while (pV < n10 * b2):
    dig = n10 % pV
    digs.insert(0, int(dig / (pV / b2)))
    pV *= b2
  for i in range (len(digs)):
    if (digs[i] > 9):
      digs[i] = chr(digs[i] + 55)
  ans = ""
  for dig in digs:
    ans += str(dig)
  return ans
print(baseConv(1000, 10, 40))
