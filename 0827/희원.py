import sys
sys.stdin = open('2.txt', 'r')

TC = int(input())

# 상(0), 하(1), 좌(2), 우(3)

for tc in range(1, TC + 1):
    n = int(input())  # 원자 수
    atom_list = [[0] * 4 for _ in range(n)]  # 원자를 받을 list
    result_power = 0  # 결과 값
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
# 원자 정보 저장
    for i in range(n):
        x, y, direc, k = map(int, input().strip().split())
        # 원자 값 저장 x(0), y(1), 방향(2), power(3)
        atom_list[i][0], atom_list[i][1], atom_list[i][2], atom_list[i][3] = x + 1000, -y + 1000, direc, k

    while atom_list:
        # 원자 폭발 가능성 확인
        for _ in range(len(atom_list)):
            # 원자 하나를 꺼낸다.
            x, y, direc, k = atom_list.pop(0)
            # 범위 내에서 나가면 폭발x => 그대로 원자 버림
            if x < 0 or y < 0 or x >= 2000 or y >= 2000:
                continue
            else:
                exclu_list = []  # 폭발 원자 번호 리스트
                # 거리가 1인 경우를 위함
                xx = x + dx[direc]
                yy = y + dy[direc]

                for j in range(len(atom_list)):
                    # x, y 가 일치하는 원자가 있을 경우 폭발 리스트에 담는다.
                    if atom_list[j][0] == x and atom_list[j][1] == y:
                        result_power += atom_list[j][3]
                        exclu_list.append(j)
                    # 거리가 1이고 방향이 반대인 원자가 있을 경우 폭발 리스트에 담는다.
                    elif atom_list[j][0] == xx and atom_list[j][1] == yy:
                        if (direc in [0, 2] and direc + 1 == atom_list[j][2]) or (direc in [1, 3] and direc - 1 == atom_list[j][2]):
                            result_power += atom_list[j][3]
                            exclu_list.append(j)

                # 폭발하는 원자가 없으면 다시 리스트에 담는다.
                if not exclu_list:
                    atom_list.append([x, y, direc, k])
                # 폭발하는 원자가 있을 경우 그 원자를 리스트에서 제거
                else:
                    result_power += k
                    while exclu_list:
                        num = exclu_list.pop()
                        atom_list.pop(num)

        # 원자 한칸씩 움직이기
        for _ in range(len(atom_list)):
            x, y, direc, k = atom_list.pop(0)
            atom_list.append([x + dx[direc], y + dy[direc], direc, k])
            
    print('#%d %d' % (tc, result_power))