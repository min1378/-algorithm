import sys
sys.stdin = open('14499.txt', 'r')
TC = int(input())

for test_case in range(1, TC+1):
    N, M, x, y, K = map(int, input().split())
    