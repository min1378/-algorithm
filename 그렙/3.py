from _collections import deque


def solution(customer, K):
    length = len(customer)
    room = set()
    waitLine = deque([]) #queue
    for i in range(length):
        if customer[i][1] == 0: # 예약 취소
            if customer[i][0] in waitLine:

                waitLine.remove(customer[i][0])
            else:
                room.remove(customer[i][0])
                if len(waitLine):
                    room.append(waitLine.popleft()) # 자동으로 대기열에서 추가
                continue


        else:
            if len(room) < K:
                room.append(customer[i][0])
            else:
                waitLine.append(customer[i][0])

    room = sorted(room)
    return room