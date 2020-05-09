def solution(dataSource, tags):
    answer = []
    dic = {}
    for data in dataSource:
        dic[data[0]] = 0
        for i in range(1, len(data)):
            if data[i] in tags:
                dic[data[0]] += 1
    dic = {key: value for key, value in dic.items() if value != 0}
    sorted_list = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    if len(sorted_list) > 10:
        sorted_list = sorted_list[:10]
    
    for el in sorted_list:
        answer.append(el[0])
    return answer

print(solution([
    ["doc1", "t1", "t2", "t3"],
    ["doc2", "t0", "t2", "t3"],
    ["doc3", "t1", "t6", "t7"],
    ["doc4", "t1", "t2", "t4"],
    ["doc5", "t6", "t100", "t8"],
],
["t1", "t2", "t3"]))