def sumsDivisibleBy( a,k):
    freq = [0]*k
    for i in range(a):
        freq[a[i]%k] += 1
    sum = freq[0]*(freq[0]-1)/2;
    i = 1
    while(i<=k//2 and i != (k-i)):
        sum+=freq[i]*freq[k-i]
        i+=1
    if(k%2==0):
        sum+=(freq[k//2]*(freq[k//2]-1)/2);
    return int(sum)
a = []
n = int(input(""))
for i in range(0,n):
    ele = int(input())
    a.append(ele)
k = 2
print(sumsDivisibleBy(a,k))
