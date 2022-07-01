
n = int(input())

for i in range(n):
    for j in range(n):
        print(j * n + i + 1, end=' ')
    print()