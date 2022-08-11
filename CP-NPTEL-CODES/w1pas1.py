
T = int(input())  # no of test cases

l = []  # each test case cache

for i in range(1, T+1):
  l.append(int(input()))

while(len(l) != 0):  # [10,5]
  n = l[0]  # 10
  stack = [n]  # [10]
  score = 0
  while(len(stack) != 0):
    for i in stack:
        x = int(i/2)
        y = i - x
        score += x*y
        stack.remove(i)
        if x !=1:
            stack.append(x)
        if y != 1:
            stack.append(y)

  print(score)
  l.pop(0)
