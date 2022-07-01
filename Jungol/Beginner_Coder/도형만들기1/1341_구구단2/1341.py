
s, e = map(int, input().split())
    
way = 1 if s < e else -1 
for j in range(s, e + way, way):
    for i in range(3):
        messages = ''
        for k in range(1, 4):
            message = f'{j} * {3 * i + k} = '
            value = j * (3 * i + k)
            message += ' ' + f'{value}' if value < 10 else f'{value}'
            messages += message + '   '
        print(messages)
    print()