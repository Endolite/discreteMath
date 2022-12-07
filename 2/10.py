# Returns 0 if disconnected and 1 if weakly connected
def connectivity(A):
  v = len(A)
  prev = [v - 1]
  next = [0]
  for i in range(v - 1):
    prev.append(i)
    next = [v - 1 - i] + next
  for i in range(v):
    if ((A[i][prev[i]] < 1) or (A[i][next[i]] < 1)):
      return ("Disconnected")
  return ("(Weakly) Connected")

A = [[0, 1, 1, 1],
      [1, 0, 1, 1],
      [1, 1, 0, 1],
      [1, 1, 1, 0]]
print(connectivity(A))