
n = int(input())

stack = []

for _ in range(n):
    order = list(input().split())
    if order[0] == 'i':
        stack.append(int(order[1]))
    elif order[0] == 'o':
        if stack:
            print(stack.pop())
            continue
        print('empty')
    elif order[0] == 'c':
        print(len(stack))