n = int(input())

if (n ^ n-1) & n == n:
    print("YES",end='')
else:
    print("NO",end='')