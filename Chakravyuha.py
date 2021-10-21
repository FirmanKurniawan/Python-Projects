CHAKRAVYUHA :

code:

print("Enter the number")
num=int(input())
l=0
h=0
r=num
c=num
n=1
v=1
count=1
a=[[0 for i in range(num)]for j in range(num)]
res=[[0,0]]
while(l<r and h<c):
    for i in range(h,c):
        a[l][i]=count
        if(a[l][i]%11==0):
            res.append([l,i])
            v+=1
        count+=1
    l+=1
    for i in range(l,r):
        a[i][c-1]=count
        if(a[i][c-1]%11==0):
            res.append([i,c-1])
            v+=1
        count+=1
    c-=1
    if(l<r):
        for i in range(c-1,h-1,-1):
            a[r-1][i]=count
            if(a[r-1][i]%11==0):
                res.append([r-1,i])
                v+=1
            count+=1
        r-=1
    if(h<c):
        for i in range(r-1,l-1,-1):
            a[i][h]=count
            if(a[i][h]%11==0):
                res.append([i,h])
                v+=1
            count+=1
        h+=1
for i in range(num):
    for j in range(num):
        print(a[i][j],end="\t")
    print("")

Output :

Enter the number
5
1	2	3	4	5	
16	17	18	19	6	
15	24	25	20	7	
14	23	22	21	8	
13	12	11	10	9	
