
while True:
    s, e = map(int, input().split())
    if 2 <= s <= 9 and 2 <= e <= 9:
        break
    print('INPUT ERROR!')

for i in range(1, 10):
    messages = ''
    way = 1 if s < e else -1 
    for j in range(s, e + way, way):
        message = f'{j} * {i} = '
        message += ' ' + f'{j * i}' if (j * i) < 10 else f'{j * i}'
        messages += message + '   '
    print(messages)