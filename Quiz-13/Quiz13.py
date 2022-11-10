def rSteps(steps, S):
  sols = [[[] for n in range(len(steps) + 1)] for s in range(S + 1)]
  for n in range(0, len(steps) + 1):
    sols[0][n].append([])

  for s in range(1, S+1):
    for n in range(1, len(steps)+1):
      without_last = sols[s][n - 1]
      if (steps[n - 1] <= s):
          with_last = [list(sol) + [steps[n-1]] for sol in sols[s - steps[n - 1]][n]]
      else:
          with_last = []
      sols[s][n] = without_last + with_last

  return sols[S][len(steps)]

print("For n=1")
print("Total number of ways for n=1 is ", len(rSteps([1,2,3], 1)))
print(rSteps([1,2,3], 1))
print()

print("For n=2")
print("Total number of ways for n=2 is ", len(rSteps([1,2,3], 2)))
print(rSteps([1,2,3], 2))
print()

print("For n=3")
print("Total number of ways for n=3 is ", len(rSteps([1,2,3], 3)))
print(rSteps([1,2,3], 3))
print()

print("For n=4")
print("Total number of ways for n=4 is ", len(rSteps([1,2,3], 4)))
print(rSteps([1,2,3], 4))
print()

print("For n=5")
print("Total number of ways n=5 is ", len(rSteps([1,2,3], 5)))
print(rSteps([1,2,3], 5))
print()