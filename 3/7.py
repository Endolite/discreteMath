import math as math
import random as rand

# Generates n Bernoulli trials with probability p
def bernDist(p, n):
  nums = []
  count = 0
  for i in range (0, n):
    if (rand.random() < p):
      nums.append(1)
      count += 1
    else:
      nums.append(0)
  print(count)
  return nums
# Generates a random permutation of the set {1,2,...,n}
def perm(n):
  N = []
  nums = []
  for i in range (1, n + 1):
    N.append(i)
  while len(N) > 0:
    i = rand.choice(N)
    nums.append(i)
    N.remove(i)
  return nums
# Simulates n repeated flips of biased coin with probability p of heads to estimate p through simulation
def coin(p, n):
  results = [['heads', 'tails'], [0, 0]]
  for i in range (0, n):
    if (rand.random() < p):
      results[1][0] += 1
    else:
      results[1][1] += 1
  pEst = results[1][0] / n
  return (results, pEst)
print(bernDist(0.5, 20))
print(perm(10))
print(coin(0.6, 1000))

