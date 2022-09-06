A = list(map(int, input().split(' ')))

n = len(A)
A.insert(0, 0)


def steps():
    if sum(A) % n != 0:
        return "Impossible"
    else:
        mean_value = sum(A)//n
        minimum_steps = 0
        for i in range(1, n+1):
            if A[i] > mean_value:
                minimum_steps += (A[i] - mean_value)
        return minimum_steps


print(steps())
