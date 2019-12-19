import sys
from collections import deque
#sys.stdin = open('4195.txt', 'r')
def union(a, b):

def find(a):

TC = int(input())
for test_case in range(1, TC+1):
    F = int(input())
    parents = {}
    for _ in range(F):
        first, second = input().split()
        if dic.get(first):
            dic[first].append(second)
        else:
            dic[first] = [second]
        if dic.get(second):
            dic[second].append(first)
        else:
            dic[second] = [first]
        group = set()
        queue = deque([])
        visited = []
        count = 0
        queue.append(first)
        while queue:
            start = queue.popleft()
            count += 1
            visited.append(start)
            if dic.get(start):
                for friend in dic[start]:
                    if friend not in visited:
                        queue.append(friend)

        print(count)