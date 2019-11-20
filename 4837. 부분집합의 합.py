import sys
sys.stdin = open("sample_input.txt", "r")

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
def somesum(temp) :
    result = 0
    for i in temp :
        result += i
    return result
T = int(input())
for test_case in range(1, T + 1):
    count = 0
    
    info = list(map(int, input().split()))
    N = info[0]
    K = info[1]
    n = len(a)
    for i in range(1<<n) :
        temp=[]
        for j in range(n+1) :
            if i & (1<<j) :
                temp.append(a[j])
        if somesum(temp) == K and len(temp) == N :
            count += 1

    print('#{} {}'.format(test_case, count))