check = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
visited = [0] * len(check)
def combination(index, members):
    if len(members) == 7: # 종료조건 7개가 되면
        print(members) # 출력
        return # 함수 종료
    for i in range(index, len(check)): # index부터 추출할 집합 끝까지 반복
        if visited[i]: # 이미 방문 => 추출했다.
            continue
        visited[i] = 1
        combination(i + 1, members + [check[i]]) # 추출한 숫자를 리스트에 넣고 재귀
        visited[i] = 0

combination(0, [])
count = 0
check = [1, 2, 3, 4, 5]
visited = [0] * len(check)
def permutation(index, members):
    global count
    if len(members) == 3: # 종료조건 7개가 되면
        print(members) # 출력
        count += 1
        return # 함수 종료
    for i in range(len(check)): # 처음부터 추출할 집합 끝까지 반복 조합과 다른점.
        if visited[i]: # 이미 방문 => 추출했다.
            continue
        visited[i] = 1
        permutation(i + 1, members + [check[i]]) # 추출한 숫자를 리스트에 넣고 재귀
        visited[i] = 0

permutation(0, [])
print(count)