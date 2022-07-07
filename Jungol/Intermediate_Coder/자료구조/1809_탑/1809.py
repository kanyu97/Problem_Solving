
n = int(input())
towers = list(map(int, input().split()))
length = max(towers)

height = [0] * (length + 1)
results = []

for i in range(n):
    results.append(height[towers[i]])
    height[:towers[i] + 1] = [i + 1] * (towers[i] + 1)

for result in results:
    print(result, end=' ')
print()
