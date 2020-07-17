def solution(x):
    list_x = list(str(x))
    sum_list_x = sum([int(i) for i in list_x])
    # s=sum([int(i) for i in str(n)])
    if x % sum_list_x:
        return False
    return True