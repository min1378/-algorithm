# import sys
# import time
# start = time.time()
# sys.stdin = open('17471.txt', 'r')
# TC = int(input())
def check_union(arr):
    count = 0
    visited2 = [False] * (N+1)
    for i in arr:
        stack = []
        if visited2[i] == False:
            stack.append(i)
        check = False
        while stack != []:
            check = True
            go = stack.pop()
            if visited2[go] == False:
                for value in dic[go]:
                    if value in arr:
                        stack.append(value)
                visited2[go] = True
        if check == True:
            count += 1
    return count


def sum_arr(arr):
    result = 0
    for i in range(len(arr)):
        result += pop_info[arr[i]]
    return result
def subset(depth, a, b, idx):
    global min_result
    if depth == len(arr):
        first = a
        second = b
        if check_union(first) == 1 and check_union(second) == 1:
            result = abs(sum_arr(first) - sum_arr(second))
            if min_result > result:
                min_result = result
        return

    subset(depth+1, a + [arr[idx]], b, idx + 1)
    subset(depth+1, a, b + [arr[idx]], idx + 1)

#for test_case in range(1, TC+1):
N = int(input())
pop_info = list(map(int, input().split()))
pop_info = [0] + pop_info
dic = {i : [] for i in range(1, N+1)}
for value in dic.values():
    temp = list(map(int, input().split()))
    value += temp[1:]
arr = [i for i in range(1, N+1)]

min_result = 9999999999
subset(0, [], [], 0)
if min_result == 9999999999:
    min_result = -1
print(min_result)
    #print("#{} {}".format(test_case,min_result))

