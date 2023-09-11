import sys
from sys import stdin
def solve(r,n):
    m=10**9+7
    res=1
    while n>0:
        if n & 1:
            res=(res*r)%m
        r=(r*r)%m
        n>>=1
    return res%m

def nthTermOfGP(n, a, r):
    m=10**9+7
    return (a*solve(r,n-1))%m
    
t = int(sys.stdin.readline().strip())
while(t > 0):
    n, a, r = map(int,input().split())
    print(nthTermOfGP(n,a,r))
    t = t - 1
    
    
    

