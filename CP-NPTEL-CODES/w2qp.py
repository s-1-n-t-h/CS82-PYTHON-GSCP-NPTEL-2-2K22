Q = list(map(int,input().split(" ")))
Q.sort(reverse=True)
n = len(Q)

Range = 1
cost = 0

for i in range(0,n):
    if i%2==0:
        cost += Q[i]*Range
    else:
        cost += Q[i]*Range
        Range += 1

print(cost*2)