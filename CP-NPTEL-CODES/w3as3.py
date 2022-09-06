A = list(map(int,input().split(' ')))

n = len(A)
A.insert(0,0)
def steps():
    if sum(A)%n != 0:
        return "Impossible"
    else:
        mean_value = sum(A)//n
        minimum_steps = 0
        for i in range(1,n+1):
            required_left_additions = max(0,(i-1)*mean_value - sum(A[1:i]))
            required_right_additions = max(0, (n-i)*mean_value - sum(A[i+1:]))
            minimum_steps = max(minimum_steps,required_left_additions+required_right_additions)
            return minimum_steps
print(steps())