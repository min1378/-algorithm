import sys
sys.stdin = open("input.txt", "r")
              
T = 10
for test_case in range(1, T + 1):
    V, E = list(map(int,input().split()))
    # E = int(input())
    temp = list(map(int, input().split()))
    for i in range(temp):
        

