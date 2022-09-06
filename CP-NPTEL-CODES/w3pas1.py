T = int(input())

for i in range(1, T+1):

    N, Q = list(map(int, input().split(" ")))

    S = list(map(int, input().split(" ")))

    Requests = []

    for j in range(1, Q+1):

        Requests.append(list(map(int, input().split(' '))))

    count = 0
    for request in Requests:

        occurenceOfSi = [i for i in range(len(S)) if S[i] == request[0]]
        occurenceOfSj = [i for i in range(len(S)) if S[i] == request[1]]
        
        for Si in occurenceOfSi:
            for Sj in occurenceOfSj:
                if Si <= Sj:
                    count += 1
                    break
            break

    print(count)