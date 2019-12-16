import sys
sys.stdin = open("input.txt", "r")

def start(ls):
    #Mode : 0 위  1오른쪽  2아래  3왼쪽 (시계방향)
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    # 0부터 리스트 끝까지 반복 
    for i in range(len(ls)):
        # 초기값, x는 0부터 +1씩 증가 y는 가장 윗줄, 지나간 자리 저장하는 체크 리스트.
        x = i
        y = 0
        check = []
        # 첫째 줄의 값이 0이라면 다음 x로 넘어감.
        if ls[y][i] == 0:
            continue
        # 1이라면 이동을 시작한다.
        else :            
            while True :
                # 아래가 기본 방향
                mode = 2
                # x가 0일때 왼쪽 인덱스는 없기 때문에 오른쪽으로 가는 방향만 조정해준다.
                if x == 0 :
                    # 체크에 없다면 지나간 자리가 아니기 때문에 이동한다. 오른쪽 방향
                    if [y,x+1] not in check and ls[y][x+1] == 1:
                        mode = 1
                # x가 제일 오른쪽일때 오른쪽 인덱스는 없기 때문에 왼쪽으로 가는 방향만 조정.
                elif x == len(ls)-1 :
                    if [y,x-1] not in check and ls[y][x-1] == 1:
                        mode = 3
                # 가장자리가 아니라면 오른쪽이나 왼쪽 길이 있을 때 방향을 조정해준다.
                else : 
                    if [y,x+1] not in check and ls[y][x+1] == 1:
                        mode = 1
                    elif [y,x-1] not in check and ls[y][x-1] == 1:
                        mode = 3
                # 체크리스트에 현재 자리를 추가한다.(지나갔다는 표시)
                check += [[y,x]]
                # 좌표를 조정한다. 
                x = x+dx[mode]
                y = y+dy[mode]
                # 만약에 y좌표가 끝에 도달하였고, 그 값이 2가 아니라면 무한루프 탈출 2라면 시작 x좌표인 i를 반환
                if y == len(ls)-1 and ls[y][x] != 2:
                    break
                if y == len(ls)-1 and ls[y][x] == 2:
                    return i
                    
                    


T = 10
for test_case in range(1, T + 1):
    temp = int(input())
    data = []
    for i in range(100) :
        line = list(map(int, input().split()))
        data.append(line)
    result = start(data)
    print('#{} {}'.format(test_case, result))

