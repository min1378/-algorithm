import sys
sys.stdin = open('1267.txt', 'r')
from collections import deque
TC = 10
for test_case in range(1, TC+1):
    V, E = map(int, input().split())
    temp = list(map(int, input().split()))
    vertex_visited_count = [0] * (V+1)
    dic = {}
    for i in range(len(temp)-1):
        if i % 2 == 0:
            if dic.get(temp[i]):
                dic[temp[i]].append(temp[i+1])
            else:
                dic[temp[i]] = [temp[i+1]]
            vertex_visited_count[temp[i+1]] += 1
    queue = deque([])
    for i in range(1, len(vertex_visited_count)):
        if vertex_visited_count[i] == 0:
            queue.append(i)

    result = []
    while queue:
        start = queue.popleft()
        result.append(start)
        if dic.get(start):
            for el in dic[start]:
                vertex_visited_count[el] -= 1
                if vertex_visited_count[el] == 0:
                    queue.append(el)

    print("#{} {}".format(test_case, ' '.join(map(str, result))))

