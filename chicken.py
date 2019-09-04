'''
https://www.acmicpc.net/problem/15686
Chicken Delivery Problem
Author: alinghi
'''
import sys
sys.stdin=open("input.txt","r")
sys.stdout=open("output.txt","w")

def init():
    N,M=map(int,input().split())
    l=[list(map(int,input().split())) for _ in range(N)]
    home,chicken=[],[]
    for i in range(N):
        for j in range(N):
            if l[i][j]==1:
                home.append((i,j))
            if l[i][j]==2:
                chicken.append((i,j))
    return N,M,l, home, chicken

def dist(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def nearest_chicken(a,chicken):
    #when list of chicken zip given
    di=150
    for i in chicken:
        di=min(di,dist(a,i))
    return di
def solver(cnt):
    if len(chicken_candidate)==M:
        ret=0
        for a in home:
            ret+=nearest_chicken(a,chicken_candidate)
        return ret
    if cnt>=len(chicken):
        return 987654321
    chicken_candidate.append(chicken[cnt])
    r1=solver(cnt+1)
    chicken_candidate.pop()
    r2 = solver(cnt + 1)
    return min(r1,r2)

chicken_candidate=[]
N,M,l,home, chicken = init()
print(solver(0))