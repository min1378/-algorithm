def check(list, n):
    if len(list) != n:
        list = "0" * (n - len(list)) + list
    return list


def check2(str):
    temp = ""
    for st in str:
        if st == "1":
            temp += "#"
        elif st == "0":
            temp += " "
    return temp


def solution(n, arr1, arr2):
    answer = []
    for i in range(n):

        result = bin(arr1[i] | arr2[i])
        result2 = result[2:]
        result3 = check(result2, n)
        result4 = check2(result3)
        answer.append(result4)
    return answer