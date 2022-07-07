
n = int(input())

def hanoi(n, s, e):
    if n == 0:
        return
    hanoi(n - 1, s, 6 - s - e)
    print(f'{n} : {s} -> {e}')
    hanoi(n - 1, 6 - s - e, e)

hanoi(n, 1, 3)