T = int(input())

for i in range(1, T+1):
    
    M = int(input())
    
    playerACards = list(map(int,input().split(' ')))

    N = int(input())

    playerBCards = list(map(int, input().split(' ')))

    if max(playerACards) >= max(playerBCards):
        print('Ankita')
    else:
        print('Biswas')
    
    if max(playerBCards) >= max(playerACards):
        print('Biswas')
    else:
        print('Ankita')
