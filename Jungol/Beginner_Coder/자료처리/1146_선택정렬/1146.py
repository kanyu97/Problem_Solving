
n = int(input())
nums = list(map(int, input().split()))

for i in range(n - 1):
    idx = nums[i:].index(min(nums[i:]))
    nums[i], nums[idx + i] = nums[idx + i], nums[i]
    for num in nums:
        print(num, end=' ')
    print()