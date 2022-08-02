T = int(input())

golden = (1+5**0.5)/2
import math

for i in range(1,T+1):

    a1, a2, b1, b2 = list(map(int,input().strip().split()))
    
    ans = 0

    for b in range(b1,b2+1):
        # a1 ... a2
        # a >= phi*b -- necessary condition for anu palyer to win
        # max(a,b) >= phi*min(a,b) -- which is same as a/b == a+b/a if a>b -- principle of golden ratio
        # b  >= phi * a
        # a <= (1 / phi) * b
        #a <= (phi - 1) * b
            # a > b          b > a
        if a1 > golden*b or (golden-1)*b > a2:  # all the values in given range forms winning pairs
            ans += (a2-a1+1)
        else:
            ans += max(0,(a2-math.floor(golden*b)))
            ans += max(0,math.floor((golden-1)*b) - a1 + 1)
    # --------|-------a1-------------|--------------a2-----|---
    # | is golden ratio a >= golden forms a winning pair always
    # if ratio falls after a2 it mean no pair can be formed

    print("Case #{}: {}".format(i,ans))
    
