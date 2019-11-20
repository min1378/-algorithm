import sys
sys.stdin = open('4880.txt', 'r')


def split(N):
    global result
    if N == 2 or N == 1:
        result.append(N)
        return
    elif N % 2 == 1 :
        return split(N//2+1), split(N//2)
    else :
        return split(N//2), split(N//2)

TC =int(input())
for test_case in range(1, TC+1):
    N = int(input())
    temp = list(map(int, input().split()))
    data = []
    data.append(temp)
    print(data,len(data))
    result = []
    stack = []
    temp1 = []
    temp2 = []

    split(10)
    print(result)
