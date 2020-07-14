def solution(n):
    answer = 0
    list_n = list(str(n))
    list_n.sort(reverse=True)
    answer = int("".join(list_n))
    return answer