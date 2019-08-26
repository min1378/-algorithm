import sys
sys.stdin = open('4871.txt', 'r')
from pprint import pprint
def serch_map(start): #행번호
    global result
    visited[start] = 1 # 방문한 곳은 1
    for next in range(1, mynode+1): #시작노드에 등록된 도착노드 검색
        if mymap[start][next] == 1 and visited[next] == 0 : # 안가본 지역
            if next == end_node:
                result = 1 #갈 수 있는 곳
                return # 검색 중단
            serch_map(next)
TC = int(input())
for tc in range(1, TC+1):
    mynode, myline = map(int, input().split()) # 할당받은 메모리 덩어리 = 객체
    mymap = [ [0] * (mynode+1) for _i in range(mynode+1)]

    #2차원 배열  생성

    for i in range(myline):
        start_node, end_node = map(int, input().split())
        mymap[start_node][end_node] = 1
    start_node, end_node = map(int, input().split()) # 검색시작과 끝

    visited = [0] * (mynode+1) #방문한곳 표시용.
    result = 0
    serch_map(start_node)
    print("#%d %d" % (tc, result))
    # debug할때 좋은 팁
    # print("---------")
    # for r in mymap:
    #     print(r)