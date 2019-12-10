import sys
sys.stdin = open('15649.txt', 'r')
TC = int(input())

def solve(temp):
    global M
    if len(temp) == M:
        print(' '.join(map(str,temp)))
        return

    for i in range(1, N+1):
        if visited[i] :
            continue
        visited[i] = 1
        solve(temp + [i])
        visited[i] = 0
for test_case in range(1, TC+1):
    N, M = map(int, input().split())
    visited = [0] * (N + 1)
    solve([])