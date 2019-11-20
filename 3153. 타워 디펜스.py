import sys
sys.stdin = open('3153.txt', 'r')
for test_case in range(1, 2):
    R, S = map(int, input().split())
    data = [list(map(str, input().split())) for _ in range(R)]
    for da in data:
        print(da)
