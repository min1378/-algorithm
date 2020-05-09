import sys
sys.stdin = open("i2775.txt", 'r')


TC = int(input())
for test_case in range(1, TC+1):
    K = int(input())
    N = int(input())
    # K층 N호의 인원수 1 2 3 // 1 3 6 // 
    data = [[0] *]