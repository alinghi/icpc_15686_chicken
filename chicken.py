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
    return N,M,l

N,M,l = init()