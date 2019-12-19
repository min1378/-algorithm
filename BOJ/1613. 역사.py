import sys
sys.stdin = open('1613.txt', 'r')
from collections import deque
N, K = map(int, input().split())
dic = {}
# 플루이드 워셜 알고리즘
D_table = [[1e9] * (N+1) for _ in range(N+1)] # 거리 테이블
V_table = [[False] * (N+1) for _ in range(N+1)] #정점 테이블
for _ in range(K):
    start, end = map(int, input().split())
    D_table[start][end] = 1
    V_table[start][end] = start
for line in D_table:
    print(line)

for line2 in V_table:
    print(line2)