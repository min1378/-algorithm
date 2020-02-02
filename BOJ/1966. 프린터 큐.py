import sys
sys.stdin = open('i1966.txt', 'r')
from collections import deque
# 풀이 함수.
def solve():
    # 알고싶은 문서의 위치를 저장하는 변수 M 
    global M
    # 문서 리스트 중에 제일 높은 중요도 check
    check = max(data)
    # 그동안 문서가 몇번 출력 되었는지 확인하는 count
    count = 0
    while True:
        # data 리스트에서 한개씩 빼서 확인한다.
        target = data.popleft()
        M -= 1
        # 중요도가 제일 크지 않다면 수행.
        if check > target:
            #  M == -1 내가 알고싶은 문서
            if M == -1:
                # 출력하지 못하였으므로 다시 뒤로 넣어준다.
                M += len(data) + 1
            data.append(target)

        # 중요도가 같다면    
        elif check == target:
            # 출력했으니 count += 1
            count += 1
            # 만약에 내가 알고 싶은 문서라면
            if M == -1:
                return count
            # 그리고 출력했으니 다시 최대값을 찾는다.
            check = max(data)
            
TC = int(input())
for test_case in range(1, TC+1):
    # 데이터 입력
    N, M = map(int, input().split())
    data = deque(list(map(int, input().split())))
    print(solve())