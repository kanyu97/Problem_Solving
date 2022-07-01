
n, m = map(int, input().split())

if m == 1:
    for i in range(1, n + 1):
        for _ in range(n):
            print(i, end=' ')
        print()
elif m == 2:
    for i in range(n):
        for j in range(1, n + 1):
            print(j if not i % 2 else n - j + 1, end=' ')
        print()
elif m == 3:
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(i * j, end=' ')
        print()