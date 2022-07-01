
n, m = map(int, input().split())

for i in range(n):
    for j in range(m):
        value = j if not i % 2 else m - j - 1
        print(m * i + value + 1, end=' ')
    print()