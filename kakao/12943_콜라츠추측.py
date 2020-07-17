def solution(num):
    count = 0
    while count < 500:
        if num % 2:
            num = num * 3 + 1
        else :
            num = num // 2
        count += 1
        if num == 1:
            return count
    
    return -1

