# # import sys
# # sys.stdin = open("input.txt", "r")
# def Permutation(arr, r):
#     # 1.

#     used = [0 for _ in range(len(arr))]

#     def generate(chosen, used):
#         # 2.
#         if len(chosen) == r:
#             print(chosen)
#             return
	
# 	# 3.
#         for i in range(len(arr)):
#             if not used[i]:
#                 chosen.append(arr[i])
#                 used[i] = 1
#                 generate(chosen, used)
#                 used[i] = 0
#                 del chosen[-1]
#     generate([], used)

# def update(the_list, n, result): 
#     templist = the_list[n:]  
#     the_list = the_list[:n]+templist
#     result.append(the_list.copy()) 
#     return the_list 
# def perm(arr):
#     source = []
#     resource = [] 
#     for i in arr :
#         source.append(i)
#     for i in range(len(arr)-1, -1, -1):
#         resource.append(arr[i])
#     result = [source.copy()]

#     while source != resource: 
#         for i in range(len(source)-1, 0, -1): 
#             if source[i] > source[i-1]: 
#                 for j in range(i, len(source)): 
#                     if source[i-1] > source[j]: 
#                         temp = source[i-1] 
#                         source[i-1] = source[j-1] 
#                         source[j-1] = temp 
#                         source = update(source, i, result) 
#                         break 
#                     elif j == len(source) - 1: 
#                         temp = source[i-1] 
#                         source[i-1] = source[j] 
#                         source[j] = temp 
#                         source = update(source, i, result) 
#                         break 
#                 break 
#     return result
def perm(a): 
    length = len(a) 
    if length == 1: 
        return [a] 
    else: 
        result = [] 
        for i in a: 
            b = a.copy() 
            b.remove(i) 
            b.sort() 
            for j in perm(b): 
                j.insert(0, i) 
                if j not in result: 
                    result.append(j) 
    return result

def connect(final):
    for i in range(len(final)):
        for j in range(len(final[i])-1):
            print(final[i][j][1],final[i][j+1][0])
            if final[i][j][1] != final[i][j+1][0] :
                del final[i]
    return final

      
T = 1
for test_case in range(1, T + 1):
    count = 1
    #c = int(input())
    # temp = list(map(int, input().split()))
    temp = [1,2,2,4,4,6]   
    info = []
    for i in range(len(temp)) :
        ls = []
        if i % 2 == 0 :
            ls.append(temp[i])
            ls.append(temp[i+1])
            info.append(ls)
    final = perm(info)
    end = connect(final)
    print('#{} {}'.format(test_case, end))