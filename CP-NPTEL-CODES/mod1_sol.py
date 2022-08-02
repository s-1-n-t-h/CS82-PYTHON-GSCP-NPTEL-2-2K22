def Reverse(L):
    count = 0
    for i in range(len(L)-1): # leaving the last element as it's automatically sorted
        j = L.index(min(L[i:])) #finding element with lowest value
        sub_array = L[i:j+1] # obtaining the sub array to be reversed
        sub_array.reverse() # reversing the sub array
        L = L[:i] + sub_array + L[j+1:] # re joining the whole array
        count += (j-i+1) # updating the cost
    return count



if __name__ == "__main__":
    N = int(input()) # total test cases
    for k in range(N):
        n = int(input()) # array length
        l = list(map(int,input().split(" "))) # taking array from input
        print("Case #"+str((k+1))+": "+str(Reverse(l))) # display the output