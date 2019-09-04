'''
https://www.acmicpc.net/problem/15686
Chicken Delivery Problme
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

N,M,l,home, chicken = init()
print(home)