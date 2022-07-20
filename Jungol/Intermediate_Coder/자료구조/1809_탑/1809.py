
n = int(input())
towers = list(map(int, input().split()))
result = []



# 2트 실패 - 시간 초과

# n = int(input())
# towers = list(map(int, input().split()))
# result = []

# for i in range(n):
#     for j in range(i - 1, -1, -1):
#         if towers[j] >= towers[i]:
#             result.append(j + 1)
#             break
#     else:
#         result.append(0)

# for value in result:
#     print(value, end=' ')
# print()
        


# 1트 실패 - 메모리 초과 에러
# n = int(input())
# towers = list(map(int, input().split()))
# length = max(towers)

# height = [0] * (length + 1)
# results = []

# for i in range(n):
#     results.append(height[towers[i]])
#     height[:towers[i] + 1] = [i + 1] * (towers[i] + 1)

# for result in results:
#     print(result, end=' ')
# print()
