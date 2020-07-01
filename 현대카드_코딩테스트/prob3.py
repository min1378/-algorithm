def solution(registered_list, new_id):
    answer = ''
    id_dict = {}
    for regis in registered_list:
        strr = ''
        digi = ''
        for i in range(len(regis)):
            if regis[i].isdigit():
                digi += regis[i]
            else:
                strr += regis[i]
        if digi == '':
            digi = 0
        digi = int(digi)
        # print(strr, digi)
        if id_dict.get(strr):
            id_dict[strr].add(digi)
        else:
            id_dict[strr] = { digi }
    # print(id_dict)
    strr_n = ''
    digi_n = ''
    for j in range(len(new_id)):
        if new_id[j].isdigit():
            digi_n += new_id[j]
        else:
            strr_n += new_id[j]
    if digi_n == '':
        digi_n = 0
    digi_n = int(digi_n)
    # print(strr_n, digi_n)
    if not id_dict.get(strr_n):
        answer = new_id
    else:
        num_dict = id_dict[strr_n]
        if digi_n not in num_dict:
            answer = new_id
        else:
            while True:
                digi_n += 1
                if digi_n not in num_dict:
                    answer = strr_n + str(digi_n)
                    break # 이거 굉장히 잘 생각해줘라!
    
    return answer


solution(["bird99", "bird98", "bird101", "gotoxy"], "bird98")