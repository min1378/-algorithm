import sys
sys.stdin = open('5102.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    V, E = map(int, input().split())
    data = []
    for i in range(E+1):
        temp = list(map(int, input().split()))
        data.append(temp)
    print(data)
    start, end = data.pop()
    print(start, end)

    dic = {}
    
    while True:
