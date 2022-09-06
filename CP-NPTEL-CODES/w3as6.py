n , m = list(map(int,input().split(' ')))
# n  - no of students
# m - no of slots
def Steps():

    slots = []

    for i in range(m):
        slots.append(list(map(int, input().split(' '))))

    slots.sort(key = lambda x: len(x) ,reverse=True)

    attended = []
    step_count = 0
    for slot in slots:
        if len(set(attended)) < n:
            attended.extend(slot)
            step_count += 1
    return step_count

print(Steps())
        

