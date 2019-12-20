import collections

TC = int(input())

def high(find):
    global count
    temp = set([])
    stack = collections.deque([find])
    visited = [False] * (N+1)
    while stack:
        start = stack.popleft()
        if visited[start]:
            continue
        visited[start] = True
        for key, value in dic.items():
            if start in value:
                stack.append(key)
                temp.add(key)

    temp2 = set([])
    stack = collections.deque([find])
    visited = [False] * (N+1)
    while stack:
        start = stack.popleft()
        if visited[start] == False:
            visited[start] = True
            if start in dic.keys() :
                for value in dic[start]:
                    temp2.add(value)
                    stack.append(value)

    if len(temp) + len(temp2) == N - 1:
        count += 1

for test_case in range(1, TC+1):
    N = int(input())
    M = int(input())
    dic = {}
    count = 0
    for _ in range(M):
        a, b = map(int, input().split())
        if b in dic.keys():
            dic[b].append(a)
        else:
            dic[b] = [a]

    for i in range(1, N+1):

        check = high(i)
        if count == N:
            break

    print("#{} {}".format(test_case, count))