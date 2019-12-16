# import sys
# sys.stdin = open('5247.txt')
import collections
TC = int(input())
def BFS(start):
    global result
    global M
    queue = collections.deque([[start, 0]])
    while queue:

        number, count = queue[0]
        if number > M + 11:
            queue.popleft()
            continue
        flag = False
        temp = []
        temp.append(number + 1)
        temp.append(number - 1)
        temp.append(number * 2)
        temp.append(number - 10)
        count += 1
        for i in temp:
            if 0 < i < M+11 and counts[i] > count:
                counts[i] = count
                flag = True
                queue.append([i, count])

        if flag == False:
            queue.popleft()

for test_case in range(1, TC+1):
    N, M = map(int, input().split())
    counts = [1e9] * (M + 11)
    BFS(N)
    print("#{} {}".format(test_case,counts[M]))