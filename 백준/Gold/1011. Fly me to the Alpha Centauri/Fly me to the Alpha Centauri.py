n = int(input())
se = [list(map(int, input().split())) for _ in range(n)]

for start, end in se:
    distance = end - start
    count = 0   # 이동횟수
    move = 1   # 이동거리
    fac_move = 3   # 이동거리 + 1 팩토리얼 값

    while distance > 0:
        distance -= move
        count += 1
        if distance == 0:
            break
        elif distance >= fac_move:
            move += 1
            fac_move += move + 1
        elif distance >= fac_move - move - 1:
            continue
        else:
            fac_move -= move + 1
            move -= 1
    print(count)    
