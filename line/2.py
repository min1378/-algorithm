def solution(answer_sheet, sheets):
    answer = 0
    for i in range(len(sheets)):
        
        sheet_size = len(sheets[i])
        for j in range(i+1, len(sheets)):
            count = 0
            continues = 0
            max_continue = 0
            for k in range(sheet_size):
                if sheets[i][k] == sheets[j][k]:
                    if answer_sheet[k] != sheets[i][k]:
                        count += 1
                        continues += 1
                    else :
                        max_continue = max(max_continue, continues)
                        continues = 0
                else:
                    max_continue = max(max_continue, continues)
                    continues = 0
            max_continue = max(max_continue, continues)
            answer = max(answer,count + max_continue ** 2)
    return answer


print(solution("24551", ["24553", "24553", "24553", "24553"]))