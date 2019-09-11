import sys
sys.stdin = open("5102.txt", "r")
TC = int(input())
for test_case in range(1, TC+1):
   node, line = list(map(int, input().split()))
   nodes = []
   for _ in range(line):
       s, b = list(map(int, input().split()))
       nodes.append([s,b])
       nodes.append([b,s])
   start, arrive = list(map(int, input().split()))
   dist = 0
   start_point = [0, start, dist]
   stop = True
   queue = [start_point]
   visited = [start]


   while True:

       start, end, dist = queue.pop(0)
       if end == arrive:
           break
       dist += 1

       for n in nodes:

           if end == n[0] and n[1] not in visited:
               print(n)
               visited.append(n[1])
               queue.append([n[0], n[1], dist])

       if len(visited) == node or queue == []:
           dist = 0
           break


   print("#{} {}".format(test_case,dist))