
pos = list(input())

pipe = 0
result = 0

for i in range(1, len(pos)):
    if pos[i] == '(':
        if pos[i - 1] == '(':
            pipe += 1
    elif pos[i] == ')':
        if pos[i - 1] == '(':
            result += pipe
        elif pos[i - 1] == ')':
            result += 1
            pipe -= 1

print(result)