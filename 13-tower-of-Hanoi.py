def toh(n,src,aux,dest,ans):
    if n==0:
        return
    toh(n-1,src,dest,aux,ans)
    ans.append([src,dest])
    toh(n-1,aux,src,dest,ans)

def towerOfHanoi(n):
    ans=[]
    toh(n,1,2,3,ans)
    return ans
