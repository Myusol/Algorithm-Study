N=int(input())

num_list=[int(input()) for _ in range(N)]
num_list.sort()

diff_list = [] # 두 수의 차 리스트 만들기

for i in range(1,N):
    diff = num_list[N-i] - num_list[N-i-1]
    diff_list.append(diff)

def gcd(x,y):
	if(y == 0):
		return x
	else:
		return gcd(y, x%y)

cd = diff_list[0]

for i in range(len(diff_list)-1):
	cd = gcd(diff_list[i],cd)
	
div_list = []

for i in range(1, int(cd**(1/2))+1):
	if (cd % i == 0):
		div_list.append(i)
		if ( (i **2 ) != cd):
			div_list.append(cd//i)
			
div_list.sort()
div_list.pop(0)
print(" ".join(map(str, div_list)))