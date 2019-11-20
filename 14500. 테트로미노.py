import sys
sys.stdin = open('14500.txt', 'r')
TC = int(input())
for test_case in range(1, TC+1):
    N, M = map(int , input().split())