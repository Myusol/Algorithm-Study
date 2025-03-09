# N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

n,s=map(int,input().split())
seq=list(map(int,input().split()))
cnt=0

def seq_sum(idx, ssum) :
    global cnt
    
    if idx >= n:
        return
    
    ssum += seq[idx]
    
    if ssum == s:
        cnt += 1
    
    seq_sum(idx+1, ssum)
    
    seq_sum(idx+1, ssum-seq[idx])
     
seq_sum(0,0)
print(cnt)