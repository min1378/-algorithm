import sys
sys.stdin = open('5185.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    N, temp = map(str, input().split())
    N = int(N)
    temp = int(temp)
    result = bin(temp)
    print(result)