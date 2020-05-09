def solution(snapshots, transactions):
    answer = []
    dic = {}
    tran_check = [0] * (10 ** 5 + 1)
    for i in range(len(snapshots)):
        dic[snapshots[i][0]] = int(snapshots[i][1])

    for tran in transactions:
        if tran_check[int(tran[0])] :
            continue
        tran_check[int(tran[0])] = 1
        if tran[2] not in dic.keys():
            dic[tran[2]] = int(tran[3])
        elif tran[1] == "SAVE":
            dic[tran[2]] += int(tran[3])
        elif tran[1] == "WITHDRAW":
            dic[tran[2]] -= int(tran[3])
            
    sorted_key = sorted(dic)

    for key in sorted_key:
        temp = []
        temp.append(key)
        temp.append(str(dic[key]))
        answer.append(temp)
    return answer


print(solution([
  ["ACCOUNT1", "100"],
  ["ACCOUNT2", "150"],
  ["ACCOUNT10", "150"]
],
[
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["2", "WITHDRAW", "ACCOUNT1", "50"],
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["4", "SAVE", "ACCOUNT3", "500"],
  ["3", "WITHDRAW", "ACCOUNT2", "30"]
]))