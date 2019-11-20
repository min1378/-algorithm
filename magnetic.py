import sys
sys.stdin = open('magnetic.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    mymap = []
    for _ in range(N): # 100 X 100 2차원 배열
        row = list(map(int, input().split())) #100개의 수를 가진 행
        mymap.append(row)

        mycount = 0 #교착횟수 저장용

        #세로 방향 검색

    for col in range(N):
        #1을 만났는지 확인하는 표식 생성
        meet1 = False
        for row in range(N):
            if mymap[row][col] == 1 :
                meet1 = True
            if meet1 and mymap[row][col] == 2:
                mycount += 1
                meet1 = False
    print("#{} {}".format(tc, mycount))