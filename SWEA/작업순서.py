import sys
sys.stdin = open("input.txt", "r")

def DFS(v):
        global visited
        if visited[v] == False:
 
            for j in range(len(mat_t[v])):
                if mat_t[v][j] == 1 and visited[v] == False:
                    DFS(j)
 
            visited[v] = True
            print(v, end=' ')


for tc in range(1, 2):
    V = 9
    E = 15
    nums = [9, 3, 7, 9, 6, 8, 8, 9, 1, 2, 1, 6, 1, 5, 2, 3, 2, 6, 2, 7, 3, 4, 3, 7, 5, 6, 6, 7, 7, 4]
    mat = [[0] * (V + 1) for _ in range(V + 1)]
    for j in range(0, len(nums), 2):
        mat[nums[j]][nums[j + 1]] = 1
    count = 0
 
    visited = [False] * (V + 1)
 
 
    
 
 
    final_nodes = []
 
    for i in range(1, len(nums), 2):
        if nums[i] not in [nums[a] for a in range(0, len(nums), 2)]:
            final_nodes += [nums[i]]

    mat_t = [[0] * (V + 1) for _ in range(V + 1)]
    for j in range(0, len(nums), 2):
        mat_t[nums[j + 1]][nums[j]] = 1




    print('#{}'.format(tc), end=' ')
 
    for num in nums:
        DFS(num)
 
    print()