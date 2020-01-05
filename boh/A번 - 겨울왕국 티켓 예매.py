import sys
sys.stdin = open('a.txt', 'r')
TC = int(input())
for test_case in range(1, TC+1):
num = int(input())
for _ in range(num):
    N, M = map(int, input().split())
    if N < 12 or M < 4:
        print(-1)
    else:
        print(11*M + 4)