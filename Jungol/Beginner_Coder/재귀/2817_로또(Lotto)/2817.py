
nums = list(map(int, input().split()))
k, nums = nums[0], nums[1:]

lotto = []
def get_lotto_nums(k, n, m):
    if m == 6:
        for i in range(6):
            print(lotto[i], end=' ')
        print()
        return
    if n > k - 1:
         return
    for i in range(n, k):
        lotto.append(nums[i])
        get_lotto_nums(k, i + 1, m + 1)
        lotto.pop()

get_lotto_nums(k, 0, 0)