import sys

sys.stdin =open('17071.txt', 'r')

from collections import deque

def solve(N, K, second):
    global result
    check = deque([[N, K, second]])

    while check:

        NN, KK, Ssecond = check.popleft()
        if KK > 500000 or NN > 500000:
            continue

        if NN == KK:
            result = Ssecond
            return

        if visited[Ssecond % 2][KK] == 1:
            result = Ssecond
            return

        Ssecond += 1
        KKK = K + Ssecond * (Ssecond + 1) // 2

        if KKK > 500000:
            return

        NNN3 = NN * 2
        if NNN3 < 500001:
            if visited[Ssecond % 2][NNN3] == 0:
                check.append([NNN3, KKK, Ssecond])
                visited[Ssecond % 2][NNN3] = 1

        if NNN3 == KKK:
            result = Ssecond
            return

        NNN2 = NN + 1
        if NNN2 < 500001:
            if visited[Ssecond % 2][NNN2] == 0:
                check.append([NNN2, KKK, Ssecond])
                visited[Ssecond % 2][NNN2] = 1

        if NNN2 == KKK:
            result = Ssecond
            return

        NNN1 = NN - 1
        if NNN1 > - 1:
            if visited[Ssecond % 2][NNN1] == 0:
                check.append([NNN1, KKK, Ssecond])
                visited[Ssecond % 2][NNN1] = 1

        if NNN1 == KKK:
            result = Ssecond
            return
# TC = int(input())
# for test_case in range(1, TC+1):
visited = [[0 for _ in range(1, 500002)] for _ in range(2)]
N, K = map(int, input().split())
second = 0
result = -1
solve(N, K, second)
print(result)