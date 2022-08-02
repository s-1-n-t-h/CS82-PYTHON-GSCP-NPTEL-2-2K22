def construct(N,C,M):
    #construct an array with elemets from M..N
    #which, when reversesorted, incurs a cost of C
    # Precondition: C is an attainable cost
    if N == 1:
        return str(M)
    else:
        if((C-1) >= N-2 and (C-1) <= N*(N-1)/2):
            # if C-1 is with in valid bounds for N-1
            # then place x at the begining and recurse directly
            # Note that the minimum increase to M+1 in recursion
            return str(M)+" "+construct(N-1,C-1,M+1)

        else:
            # If we are not in the "easy" case above,
            # then reduce C by as much as you need to to be
            # within valid bounds in recursion:
            delta = int(C - N*(N-1)/2 + 1)

            # Now recurse with the appropriately adjusted cost
            # (i.e, C-delta) and updated minimum (M+1):
            y = construct(N-1, C - delta, M+1)

            # Sneak M to the array obtained from recursion:
            smallarr = y.split(" ")
            newarr = [str(M)]
            newarr.extend(smallarr)

            # Reverse the subarray upto delta so that the cost of
            # getting M in its correct place is exactly delta,
            # and the reversal that puts M in its correct place
            # leads to the array "smallarr" which had cost C-delta
            # by the correctness of recursion,
            # so that the total cost is C, as desired:

            ans = " ".join(newarr[:delta][::-1] + newarr[delta:])
            return ans
             
    
if __name__ == "__main__":
    T = int(input()) # no of test cases
    for k in range(1,T+1):
        # taking input for size & cost required
        size_and_cost = list(map(int, input().split(" ")))
        N = size_and_cost[0] #size
        C = size_and_cost[1] #cost
        if (C < N-1) or (C > N*(N+1)/2 -1):
            #if required cost is above the upper bound or below the lower bound, such an array can't be permuted
            print("Case #"+str(k)+": IMPOSSIBLE")
        else:
            #otherwisee invoke recursive mechanism
            A = construct(N,C,1)
            print("Case #"+str(k)+": "+str(A))
