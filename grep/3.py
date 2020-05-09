from collections import deque

def solution(customers, K):
    answer = []
    room = [0] * K
    is_empty = [i for i in range(K)]
    where_room = [0] * 1000001
    queue = deque([])
    for customer in customers:
        guest_number = customer[0]
        reservation_number = customer[1]
        if reservation_number == 1 :
            if len(is_empty):
                room_number = is_empty.pop()
                room[room_number] = guest_number
                where_room[guest_number] = room_number
            else:
                queue.append(guest_number)
        if reservation_number == 0:
            now_room = where_room[guest_number]
            room[now_room] = 0
            is_empty.append(now_room)
            where_room[guest_number] = 0
            if len(queue):
                nextNumber = queue.popleft()
                room_number = is_empty.pop()
                room[room_number] = nextNumber
                where_room[nextNumber] = room_number
    room.sort()
    for i in range(len(room)):
        if room[i] > 0:
            room = room[i:]
            break
    return room

print(solution([[2, 1], [3, 1], [4, 1], [3, 0], [1, 1], [2, 0], [4, 0], [2, 1]], 3))