
n, m = map(int, input().split())   # n: λμ΄, m: λλΉ

for i in range(n):
    for j in range(m):
        print(m * i + j + 1, end=' ')
    print()