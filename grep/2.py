def search(el, visited, card, count):
    for i in range(len(card)):
        for j in range(len(card[i])):
            if visited[i][j] :
                continue
            if el == card[i][j]:
                visited[i][j] = 1
                count[i] += 1
                return True, visited, count
    return False, visited, count
            


def solution(card, word):
    answer = []
    for check in word:
        count = [0, 0, 0]
        visited = [[0] * 8 for _ in range(3)]
        flag2 = False
        for el in check:
            flag, visited, count = search(el, visited, card, count)
            if flag == False:
                flag2 = False
                break
        if flag2 == False:
            continue
                
        if 0 not in count and flag:
            answer.append(check)

    if len(answer) == 0:
        answer.append("-1")
    return answer

print(solution(["ABACDEFG", "NOPQRSTU", "HIJKLKMM"], ["GPQM","GPMZ", "EFU", "MMNA"]))
print(solution(["AABBCCDD", "KKKKJJJJ", "MOMOMOMO"], ["AAAKKKKKMMMMM", "ABCDKJ"]))