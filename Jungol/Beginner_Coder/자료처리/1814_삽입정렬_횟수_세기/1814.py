
n = int(input())
nums = list(map(int, input().split()))
result = 0

for i in range(1, n):
    idx = i
    for j in range(0, i):
        if nums[i] < nums[j]:
            idx = j
            break
    nums = nums[:idx] + nums[i:i+1] + nums[idx:i] + nums[i+1:]
    result += abs(i - idx)
print(result)