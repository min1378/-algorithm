import sys
sys.stdin = open('5214.txt', 'r')
N, K, M = map(int, input().split())

dic ={}
for _ in range(M):
    
    if dic.keys()