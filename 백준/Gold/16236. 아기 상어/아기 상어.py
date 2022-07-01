n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]

move = 0
size, cnt = 2, 2
pos_i, pos_j = 0, 0   # 시작 위치

# 시작 위치 찾기
for i in range(n):
    for j in range(n):
        if area[i][j] == 9:
            pos_i, pos_j = i, j


# 거리를 늘려가면서 상단 중 좌측부터 탐색
delta = [[-1, 0], [0, -1], [0, 1], [1, 0]]   # 상, 좌, 우, 하 순으로 탐색

while True:
    queue = []
    area_check = [[0] * n for _ in range(n)]   # 지나간 자리 체크를 위한 list
    area_check[pos_i][pos_j] = 1

    for delta_i, delta_j in delta:
        if 0 <= pos_i + delta_i < n and 0 <= pos_j + delta_j < n:
            queue.append([pos_i + delta_i, pos_j + delta_j])
            area_check[pos_i + delta_i][pos_j + delta_j] = 1
    queue.append(['check_point', 1])

    while queue:
        next_pos = queue.pop(0)
        next_i, next_j = next_pos[0], next_pos[1]

        # 이동거리를 구하기 위한 check point
        if next_i == 'check_point' and len(queue) > 0:
            queue.append([next_i, next_j + 1])
            continue
        elif next_i == 'check_point' and len(queue) == 0:
            continue

        # 물고기가 없거나, 같은 크기의 물고기가 있을 경우
        if area[next_i][next_j] == size or area[next_i][next_j] == 0:
            area_check[next_i][next_j] = 1
            # 벗어난 좌표가 아니고, 지나간 자리인지 체크한 뒤 탐색 큐에 추가
            for delta_i, delta_j in delta:
                if 0 <= next_i + delta_i < n and 0 <= next_j + delta_j < n and area_check[next_i + delta_i][next_j + delta_j] == 0:
                    queue.append([next_i + delta_i, next_j + delta_j])
                    area_check[next_i + delta_i][next_j + delta_j] = 1

        # 작은 물고기가 있을 경우
        elif area[next_i][next_j] < size:
            area[pos_i][pos_j]= 0

            # check point까지 pop
            # 1. 이동거리 확인을 위해
            # 2. 같은 이동거리 안에 상단 혹은 좌측 물고기가 존재하는지 확인하기 위해
            while True:
                check = queue.pop(0)
                c1, c2 = check[0], check[1]
                if c1 == 'check_point':
                    move += c2
                    break
                if 0 < area[c1][c2] < size:
                    if (c1 < next_i) or (c1 == next_i and c2 < next_j):
                        next_i, next_j = c1, c2
            area[next_i][next_j] = 9

            # 물고기 위치, 크기 등 조정
            pos_i, pos_j = next_i, next_j
            cnt -= 1
            if cnt == 0:
                size += 1
                cnt = size
            break

        # 더 큰 물고기가 있을 경우
        elif area[next_i][next_j] > size:
            area_check[next_i][next_j] = 1

    # 더 이상 탐색이 불가능할 경우 이동거리 출력 후 종료
    else:
        print(move)
        break