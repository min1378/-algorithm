def solution(m, k):
    lst = []
    for i in m:
        lst.append(i)
    lst2 = []
    for i in k:
        lst2.append(i)
    checked=[]
    index = 0
    for j in range(len(lst2)):
        for i in range(index, len(lst)):
          if lst[i] == lst2[j]:
            lst[i] = "0"
            index = i + 1
            break
    answer = '' 
    # for i in checked:
    #     if i != '0':
    #         answer += i
    # print(answer, "check2")
    print(lst)
    for i in lst:
        if i != '0':
            answer += i
    return answer


print(solution("kkaxbycyz", "abc"))
print(solution("acbbcdc", "abc"))