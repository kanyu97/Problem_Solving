
n = int(input())

queue = []

for _ in range(n):
    order = list(input().split())
    if order[0] == 'i':
        queue.append(int(order[1]))
    elif order[0] == 'o':
        if queue:
            print(queue.pop(0))
            continue
        print('empty')
    elif order[0] == 'c':
        print(len(queue))