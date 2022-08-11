n = int(input())  # no of test cases

for i in range(1, n+1):
  N, X = list(map(int, input().split(" ")))

  L = list(map(int, input().split(" ")))
  L.sort()
  l1 = L[0:N]
  l2 = L[N:]

  diff = []

  for j in range(len(l1)):
    diff.append(abs(l1[j]-l2[j]))

  satisfied = list(map(lambda x: x >= X, diff)) # verifying if atleast one person is not enough taller
 
  if False in satisfied:
    print("NO")
  else:
    print("YES")
