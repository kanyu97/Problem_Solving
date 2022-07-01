
n, m = map(int, input().split())   # n: 높이, m: 너비

for i in range(n):
    for j in range(m):
        print(m * i + j + 1, end=' ')
    print()