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
            # if lst[i] == lst2[j]:
            #     lst[i] = "0"
            #     lst2[j] = '*'
            # else:
            #     if lst2[j] != '*':
            #         checked.append(lst[i])
            #         lst[i] = "0"
            #         # j=j+1
    # print(m, k) 
    # print(checked, lst, lst2)
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