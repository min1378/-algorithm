import sys
import time

start = time.time()  # 시작 시간 저장

# 작업 코드



sys.stdin = open('17281.txt', 'r')
#TC = int(input())
# def solve():
#     global temp_score
#     start_number = 0
#     for ining_number in range(N):
#         base = [0, 0, 0, 0]
#         out_count = 0
#         while True:
#             if out_count == 3:
#                 temp_score += base[0]
#                 break
#             bat = inning[ining_number][temp[start_number]]
#             start_number = (start_number + 1) % 9
#             if bat == 0:
#                 out_count += 1
#                 continue
#
#             elif bat == 1:
#                 for i in range(len(base)-1, 0, -1):
#                     if i == 3:
#                         if base[i] == 1:
#                             base[i] = 0
#                             base[0] += 1
#                     elif base[i] == 1:
#                         base[i+1] = 1
#                         base[i] = 0
#                 base[1] = 1
#             elif bat == 2:
#                 for i in range(len(base)-1, 0, -1):
#                     if i == 2 or i == 3:
#                         if base[i] == 1:
#                             base[i] = 0
#                             base[0] += 1
#                     elif base[i] == 1:
#                         base[i+2] = 1
#                         base[i] = 0
#                 base[2] = 1
#             elif bat == 3:
#                 for i in range(len(base)-1, 0, -1):
#                     if base[i] == 1:
#                         base[0] += 1
#                         base[i] = 0
#                 base[3] = 1
#
#             elif bat == 4:
#                 for i in range(len(base)-1, 0, -1):
#                     if base[i] == 1:
#                         base[0] += 1
#                         base[i] = 0
#                 base[0] += 1


# for test_case in range(1, TC+1):
N = int(input())
inning = [list(map(int, input().split())) for _ in range(N)]
p = [1, 2, 3, 4, 5, 6, 7, 8]
isEnd = True
score = 0
while True:

    temp = p[:3] + [0] + p[3:]


    temp_score = 0
    index = 0
    for inning_number in range(N):
        out = 0
        one, two, three = 0, 0, 0
        while out != 3:
            now = inning[inning_number][temp[index]]
            if now == 0:
                out += 1
            elif now == 1:
                temp_score += three
                one, two, three = 1, one, two
            elif now == 2:
                temp_score += three + two
                one, two, three = 0, 1, one
            elif now == 3:
                temp_score += three + two + one
                one, two, three = 0, 0, 1
            else:
                temp_score += one + two + three + 1
                one, two, three = 0, 0, 0

            index = (index + 1) % 9
    #solve()
    score = max(score, temp_score)

    for i in range(7, -1, -1):
        # 2. 뒤에서부터 탐색하여 오름차순으로 정렬되어있을 때 왼쪽 인덱스를 저장

        if i == 0:  # 3. 만약 내림차순으로 정렬이 되어있다면 더 이상 반복할 필요가 없으므로 종료
            isEnd = False
            break
        if p[i - 1] < p[i]:
            idx = i - 1  # 4. 인덱스 저장
            break
    if not isEnd:
        break
    # 5. idx자리에 있는 값보다 큰 p[k]를 찾아 p[idx], p[k] 스왑
    for k in range(7, -1, -1):
        if p[idx] < p[k]:
            p[idx], p[k] = p[k], p[idx]
            break
    # 6. idx+1 부터 끝까지의 배열을 오름차순으로 정렬
    # 7. 역순으로 정렬하는 것과 같은 말
    my_end_idx = 7
    idx += 1
    while idx < my_end_idx:
        p[idx], p[my_end_idx] = p[my_end_idx], p[idx]
        idx += 1
        my_end_idx -= 1

print(score)
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간