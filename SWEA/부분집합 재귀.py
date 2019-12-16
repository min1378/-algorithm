my_list = [3,4,2,4,5 ,6 ,7 ,8 ,9 ]
def subset(depth, a, b, idx, lis):
    if depth ==len(lis):
        temp.append((a,b))
        return
    subset(depth+1, a+[lis[idx]], b, idx+1, lis)
    subset(depth + 1, a, b+[lis[idx]], idx + 1, lis)
temp = []
subset(0,[],[],0,my_list)
print(temp)