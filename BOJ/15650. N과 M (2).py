import sys
sys.stdin = open('15650.txt', 'r')

def solve(temp, start):
    global M
    if len(temp) == M:
        result = ''
        for i in temp:
            result += str(i) + ' '
        print(result)
        return

    for i in range(start, N+1):
        solve(temp + [i], i + 1)

TC = int(input())
for test_case in range(1, TC+1):
    N, M = map(int, input().split())
    solve([], 1)