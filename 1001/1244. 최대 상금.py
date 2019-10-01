import sys
import copy
sys.stdin = open('1244.txt', 'r')
def permu(arr, count):
    print(arr, count)
    # arr에 담긴 숫자를 비교하기 위해 인트형으로 바꿔준다.
    a = int(''.join(arr))
    #만약에 체크에 담긴 숫자보다 작으면 컷. 제일 큰 수만 필요하기 때문에
    if check[count] > a:
        return
    # 체크에 담긴 숫자보다 크면 값을 넣는다.
    check[count] = a
    #만약에 count가 바꾼 횟수에 도달하였다면 끝냄.
    if count == N :
        return
    for i in range(size): # 인덱스 0, 1, 2, 3, 4 ...
        for j in range(i+1, size): # 다음 인덱스부터 마지막 인덱스까지
            arr[i], arr[j] = arr[j], arr[i] # 바꾼다.
            permu(arr,count+1) # 횟수를 늘리고 다시 재귀돌린다.
            arr[j], arr[i] = arr[i], arr[j]
TC = int(input())
for test_case in range(1, TC+1):
    data, N = map(str, input().split())
    data = list(data)
    size = len(data)
    N = int(N)
    check = [0] * (N+1)
    print(data)
    permu(data, 0)

    print("#{} {}".format(test_case, check[-1])) #최대값은 check의 마지막 리스트에 저장되어있으므로.