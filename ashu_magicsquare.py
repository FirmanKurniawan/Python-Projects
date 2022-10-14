def magic_sqr(n):

    magicSqr=[[0 for i in range(n)] for j in range(n)]

    i=n//2
    j=n-1
    num =n*n
    count=1
    while(count<=num):
        if i==-1 and j==n:
            j=n-2
            i=0
        else:
            if i<0:
                i=n-1
            if j==n:
                j=0
        if magicSqr[i][j]!=0:
            j = j-2
            i = i+1
            continue
        else:
            magicSqr[i][j]=count
            count+=1
        i=i-1
        j=j+1
    # print magicSqr
    for x in range(len(magicSqr)):
        print(*magicSqr[x],end=f" = {int(n*(n**2+1)/2)}\n")
    m=int(n*(n**2+1)/2)
    for i in range(n+1):
        print(f"{m} ",end="")
magic_sqr(int(input()))
