TC=int(input())
for n in range(TC):
    N=int(input())
    L=list(map(int,input().split()))
    A=[]
    cnt=[0]*(max(L)+1)
    for num in range(len(L)):
        cnt[L[num]]+=1
    for go in range(len(cnt)):
        if cnt[go] == 1 and L.index(go) % 2==0:
            A.extend([L[L.index(go)],L[L.index(go)+1]])
    while len(A)!=len(L):
        for plus in range(0,len(L),2):
            if A[-1]==L[plus]:
                A.extend([L[plus],L[plus+1]])
    print("#%d"%(n+1),end=" ")
    for i in range(2*N):print(A[i], end=" ")
    print()