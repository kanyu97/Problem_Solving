
M = int(input())
postfix = list(input().split())

stack = []
oper = ['+', '-', '*', '/']

for c in postfix:
    if c in oper:
        if c == '+':
            stack.append(stack.pop() + stack.pop())
        elif c == '-':
            right, left = stack.pop(), stack.pop()
            stack.append(left - right)
        elif c == '*':
            stack.append(stack.pop() * stack.pop())
        elif c == '/':
            right, left = stack.pop(), stack.pop()
            stack.append(left // right)
    else:
        stack.append(int(c))

print(stack[0])
