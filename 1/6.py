# Prints a Paxcal triangle of height x
def pascal(x):
  sol = [["" for i in range(x + 1)] for j in range(x + 1)]
  for i in range(x + 1):
    for j in range(x + 1):
      if (j == 0 or j == i):
        sol[i][j] = 1
      else:
        sol[i][j] = sol[i - 1][j - 1] + sol[i - 1][j]
    for j in range(x + 1):
      print(sol[i][j], end = " ");
    print();
arr = pascal(8)
