import sys
def merge_sort(arr,p,r):
    if(p<r):
        q=(p+r)//2
        merge_sort(arr,p,q)
        merge_sort(arr,q+1,r)
        merge(arr,p,q,r)
def merge(arr,p,q,r):
    global cnt, res
    tmp=[]
    i,j=p,q+1
    while i<=q and j<=r:
        if arr[i]<=arr[j]:
            tmp.append(arr[i])
            i+=1
        else:
            tmp.append(arr[j])
            j+=1
    while i<=q:
        tmp.append(arr[i])
        i+=1
    while j<=r:
        tmp.append(arr[j])
        j+=1
    for t in range(len(tmp)):
        arr[p+t] = tmp[t]
        cnt+=1
        if cnt==K:
            res=arr[p+t]
            return
N,K=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
cnt=0
res=-1
merge_sort(arr,0,N-1)
print(res)