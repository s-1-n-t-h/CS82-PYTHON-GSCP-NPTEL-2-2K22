n = int(input())

for i in range(1,n+1):
    N, Q = list(map(int,input().split(" ")))
    packetsInBoxes = list(map(int,input().split(" ")))
    
    packetsInBoxes.sort(reverse=True)

    for j in range(1,Q+1):  
        q = int(input())
        count = 0;sum = 0
        for box in packetsInBoxes:
            count += 1
            sum += box
            if sum >= q:
                print(count)
                break
        else:
            print(-1)




